from __future__ import annotations

import re
import streamlit as st


def normalize_math(text: str) -> str:
    text = re.sub(
        r"\\\[\s*(.*?)\s*\\\]",
        lambda match: f"\n$$\n{match.group(1).strip()}\n$$\n",
        text or "",
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\\\(\s*(.*?)\s*\\\)",
        lambda match: f"${match.group(1).strip()}$",
        text,
        flags=re.DOTALL,
    )
    return text


def render_messages(messages: list[dict]) -> None:
    for message in messages[1:]:
        avatar = "🧭" if message["role"] == "assistant" else "🧑‍🎓"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(normalize_math(message["content"]))
