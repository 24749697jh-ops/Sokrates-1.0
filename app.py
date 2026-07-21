from __future__ import annotations

import base64
import io
import mimetypes
import os
from typing import Any

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from streamlit_paste_button import paste_image_button

from config import (
    APP_ICON,
    APP_TITLE,
    MAX_FILE_SIZE_MB,
    MAX_OUTPUT_TOKENS,
    MODEL,
    SUPPORTED_UPLOAD_TYPES,
)
from engine.teacher_engine import (
    build_teacher_prompt,
    fallback_question,
    topic_key_for,
)
from ui.chat import render_messages
from ui.formula_sidebar import render_formula_sidebar
from ui.math_editor import readable_to_latex, render_math_editor
from ui.theme import inject_theme

load_dotenv()

st.set_page_config(
    page_title=f"{APP_TITLE} – Mathe-Lerncoach",
    page_icon=APP_ICON,
    layout="wide",
)

inject_theme()


def ensure_state() -> None:
    defaults = {
        "messages": [],
        "task_started": False,
        "task_text": "",
        "task_input": "",
        "reply_input": "",
        "uploaded_name": None,
        "uploaded_bytes": None,
        "uploaded_mime": None,
        "help_level": 1,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_session() -> None:
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    ensure_state()


def data_url(file_bytes: bytes, mime_type: str) -> str:
    encoded = base64.b64encode(file_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def store_pasted_image(image: Any) -> None:
    buffer = io.BytesIO()
    image.convert("RGB").save(buffer, format="PNG")
    st.session_state.uploaded_name = "goodnotes-zwischenablage.png"
    st.session_state.uploaded_bytes = buffer.getvalue()
    st.session_state.uploaded_mime = "image/png"


def build_first_user_content(task_text: str) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] = [
        {
            "type": "input_text",
            "text": (
                "Hier ist meine Mathematikaufgabe. Analysiere sie genau und "
                "beginne sofort mit einer fachlich passenden Frage. Frage nie, "
                "ob du helfen oder die Aufgabe lösen sollst.\n\n"
                f"Aufgabe:\n{task_text or '(nur Datei/Bild)'}"
            ),
        }
    ]

    if st.session_state.uploaded_bytes:
        encoded = data_url(
            st.session_state.uploaded_bytes,
            st.session_state.uploaded_mime,
        )
        if st.session_state.uploaded_mime.startswith("image/"):
            content.append(
                {"type": "input_image", "image_url": encoded, "detail": "high"}
            )
        else:
            item: dict[str, Any] = {
                "type": "input_file",
                "filename": st.session_state.uploaded_name,
                "file_data": encoded,
            }
            if st.session_state.uploaded_mime == "application/pdf":
                item["detail"] = "high"
            content.append(item)

    return content


def build_api_input() -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for index, message in enumerate(st.session_state.messages):
        if index == 0 and message["role"] == "user":
            result.append(
                {
                    "role": "user",
                    "content": build_first_user_content(message["content"]),
                }
            )
        else:
            result.append(
                {"role": message["role"], "content": message["content"]}
            )
    return result


def get_answer() -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(
        model=MODEL,
        instructions=build_teacher_prompt(
            st.session_state.task_text,
            st.session_state.messages,
            st.session_state.help_level,
        ),
        input=build_api_input(),
        max_output_tokens=MAX_OUTPUT_TOKENS,
    )
    answer = response.output_text.strip()
    return answer or fallback_question(
        st.session_state.task_text,
        st.session_state.messages,
    )


def send_message(text: str) -> None:
    cleaned = text.strip()
    if not cleaned:
        return

    latex = readable_to_latex(cleaned)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": (
                f"Mein Gedanke oder Rechenschritt lautet: {cleaned}\n\n"
                f"Mathematisch dargestellt:\n$${latex}$$"
            ),
        }
    )

    with st.spinner("Sokrates denkt über deinen Schritt nach ..."):
        answer = get_answer()

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )


ensure_state()

st.markdown(
    """
    <div class="hero">
      <h1>🧭 Sokrates 1.0</h1>
      <p><em>Ich begleite dich – denken musst du selbst.</em></p>
      <p>Verstehen → Planen → Rechnen → Prüfen</p>
    </div>
    """,
    unsafe_allow_html=True,
)

api_key = os.getenv("OPENAI_API_KEY")

with st.sidebar:
    st.header("Sokrates")
    if api_key:
        st.success("✅ Sokrates ist bereit")
    else:
        st.error("Der OpenAI-Schlüssel fehlt.")
    st.caption("Sokrates gibt keine fertigen Lösungen aus.")

    if st.button("Neue Aufgabe", use_container_width=True):
        reset_session()
        st.rerun()

    if st.session_state.task_started:
        st.divider()
        render_formula_sidebar(
            topic_key_for(
                st.session_state.task_text,
                st.session_state.messages,
            ),
            "reply_input",
        )
    else:
        st.divider()
        render_formula_sidebar("general", "task_input")


if not st.session_state.task_started:
    task_text = render_math_editor(
        "task_input",
        "Aufgabe eingeben",
        "Schreibe oder kopiere deine Mathematikaufgabe hier hinein.",
        "Aufgabe übernehmen",
    )

    st.markdown("### Aus GoodNotes einfügen")
    st.caption("Mit dem Lasso markieren, kopieren und hier einfügen.")
    paste_result = paste_image_button(
        label="📋 Aus Zwischenablage einfügen",
        key="goodnotes_paste",
        errors="raise",
    )
    if paste_result.image_data is not None:
        store_pasted_image(paste_result.image_data)
        st.success("Die Aufgabe aus GoodNotes wurde eingefügt.")
        st.image(paste_result.image_data, use_container_width=True)

    upload = st.file_uploader(
        "Oder Datei hochladen",
        type=SUPPORTED_UPLOAD_TYPES,
        help=f"Maximal {MAX_FILE_SIZE_MB} MB.",
    )
    if upload is not None:
        size_mb = len(upload.getvalue()) / (1024 * 1024)
        if size_mb > MAX_FILE_SIZE_MB:
            st.error(f"Die Datei ist größer als {MAX_FILE_SIZE_MB} MB.")
        else:
            st.session_state.uploaded_name = upload.name
            st.session_state.uploaded_bytes = upload.getvalue()
            st.session_state.uploaded_mime = (
                upload.type
                or mimetypes.guess_type(upload.name)[0]
                or "application/octet-stream"
            )
            st.success(f"Datei bereit: {upload.name}")

    if st.button("Mit Sokrates beginnen", type="primary", use_container_width=True):
        task = st.session_state.get("task_input", "").strip()
        has_task = bool(task) or st.session_state.uploaded_bytes is not None

        if not api_key:
            st.error("Der OpenAI-Schlüssel wurde auf dem Server nicht eingerichtet.")
        elif not has_task:
            st.error("Bitte gib eine Aufgabe ein oder lade eine Datei hoch.")
        else:
            st.session_state.task_text = task
            st.session_state.messages = [{"role": "user", "content": task}]
            st.session_state.task_started = True
            st.session_state.task_input = ""
            try:
                st.session_state.messages.append(
                    {"role": "assistant", "content": get_answer()}
                )
                st.rerun()
            except Exception as exc:
                st.session_state.task_started = False
                st.error(f"Die Anfrage konnte nicht verarbeitet werden: {exc}")

else:
    render_messages(st.session_state.messages)

    st.caption(f"Hilfestufe {st.session_state.help_level} von 4")
    c1, c2 = st.columns(2)

    with c1:
        if st.button("💡 Kleiner Hinweis", use_container_width=True):
            st.session_state.help_level = min(
                4,
                st.session_state.help_level + 1,
            )
            try:
                send_message(
                    "Ich brauche einen etwas deutlicheren Hinweis, "
                    "aber noch keine vollständige Lösung."
                )
                st.rerun()
            except Exception as exc:
                st.error(f"Fehler: {exc}")

    with c2:
        if st.button("↩️ Hilfestufe zurücksetzen", use_container_width=True):
            st.session_state.help_level = 1
            st.rerun()

    st.divider()
    reply = render_math_editor(
        "reply_input",
        "Dein nächster Schritt",
        "Schreibe deinen Gedanken oder Rechenschritt.",
        "An Sokrates senden",
    )

    if reply:
        try:
            send_message(reply)
            st.session_state.reply_input = ""
            st.rerun()
        except Exception as exc:
            st.error(f"Die Anfrage konnte nicht verarbeitet werden: {exc}")
