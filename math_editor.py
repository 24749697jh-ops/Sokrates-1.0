from __future__ import annotations

import re
import streamlit as st


GREEK_MAP = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta",
    "θ": r"\theta", "λ": r"\lambda", "μ": r"\mu", "π": r"\pi",
    "ρ": r"\rho", "σ": r"\sigma", "φ": r"\varphi", "ω": r"\omega",
    "Δ": r"\Delta", "Σ": r"\Sigma", "Π": r"\Pi", "Ω": r"\Omega",
}

QUICK_KEYS = (
    ("²", "²"), ("³", "³"), ("√", "√("), ("π", "π"),
    ("α", "α"), ("β", "β"), ("γ", "γ"), ("Δ", "Δ"),
)

OPERATOR_KEYS = (
    ("+", " + "), ("−", " − "), ("×", " · "), ("÷", " : "),
    ("=", " = "), ("≠", " ≠ "), ("≤", " ≤ "), ("≥", " ≥ "),
)

MORE_KEYS = (
    ("(", "("), (")", ")"), ("[", "["), ("]", "]"),
    ("%", "%"), ("°", "°"), ("≈", " ≈ "), ("±", " ± "),
)


def readable_to_latex(text: str) -> str:
    result = text.strip()
    previous = None
    while previous != result:
        previous = result
        result = re.sub(r"\(([^()]*)\)\s*/\s*\(([^()]*)\)", r"\\frac{\1}{\2}", result)
        result = re.sub(r"\(([^()]*)\)\s*\^\s*\(([^()]*)\)", r"{\1}^{\2}", result)
        result = re.sub(r"√\(([^()]*)\)", r"\\sqrt{\1}", result)

    for old, new in (
        ("·", r"\cdot "), ("−", "-"), ("≠", r"\neq "),
        ("≈", r"\approx "), ("≤", r"\le "), ("≥", r"\ge "),
        ("±", r"\pm "), ("²", "^2"), ("³", "^3"),
        ("°", r"^\circ"), ("ₛ", "_s"),
    ):
        result = result.replace(old, new)

    for symbol, latex in GREEK_MAP.items():
        result = result.replace(symbol, latex + " ")
    return result


def _append(buffer_key: str, value: str) -> None:
    st.session_state[buffer_key] = st.session_state.get(buffer_key, "") + value


def _delete(buffer_key: str) -> None:
    st.session_state[buffer_key] = st.session_state.get(buffer_key, "")[:-1]


def _clear(buffer_key: str) -> None:
    st.session_state[buffer_key] = ""


def _row(keys, prefix: str, buffer_key: str, columns: int = 8) -> None:
    cols = st.columns(columns)
    for index, (label, value) in enumerate(keys):
        with cols[index % columns]:
            st.button(
                label,
                key=f"{prefix}_{buffer_key}_{index}",
                use_container_width=True,
                on_click=_append,
                args=(buffer_key, value),
            )


def render_math_editor(
    target_key: str,
    label: str,
    placeholder: str,
    send_label: str,
) -> str | None:
    buffer_key = f"{target_key}_math"
    st.session_state.setdefault(buffer_key, "")

    st.markdown(f"### {label}")
    manual_text = st.text_area(
        label,
        key=target_key,
        height=115,
        placeholder=placeholder,
        label_visibility="collapsed",
    )

    st.caption("Mathematische Zeichen")
    math_text = st.text_input(
        "Mathematische Zeichen",
        key=buffer_key,
        placeholder="Zeichen aus der Tastatur erscheinen hier.",
        label_visibility="collapsed",
    )

    _row(QUICK_KEYS, "quick", buffer_key)
    _row(OPERATOR_KEYS, "operator", buffer_key)

    with st.expander("Weitere Zeichen und Formelvorlagen", expanded=False):
        _row(MORE_KEYS, "more", buffer_key, columns=4)

    combined = " ".join(
        part for part in (manual_text.strip(), math_text.strip()) if part
    ).strip()

    if combined:
        st.markdown("**Vorschau**")
        st.markdown(combined)

    c1, c2, c3 = st.columns(3)
    with c1:
        send = st.button(
            send_label,
            type="primary",
            use_container_width=True,
            disabled=(combined == ""),
            key=f"{target_key}_send",
        )
    with c2:
        st.button(
            "⌫ Mathe",
            use_container_width=True,
            disabled=(math_text == ""),
            key=f"{target_key}_delete_math",
            on_click=_delete,
            args=(buffer_key,),
        )
    with c3:
        st.button(
            "Mathe löschen",
            use_container_width=True,
            disabled=(math_text == ""),
            key=f"{target_key}_clear_math",
            on_click=_clear,
            args=(buffer_key,),
        )

    return combined if send else None
