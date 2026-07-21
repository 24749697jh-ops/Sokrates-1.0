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
        ("·", r"\cdot "),
        ("−", "-"),
        ("≠", r"\neq "),
        ("≈", r"\approx "),
        ("≤", r"\le "),
        ("≥", r"\ge "),
        ("±", r"\pm "),
        ("²", "^2"),
        ("³", "^3"),
        ("°", r"^\circ"),
        ("ₛ", "_s"),
    ):
        result = result.replace(old, new)

    for symbol, latex in GREEK_MAP.items():
        result = result.replace(symbol, latex + " ")

    return result


def _append_math(buffer_key: str, value: str) -> None:
    st.session_state[buffer_key] = st.session_state.get(buffer_key, "") + value


def _delete_math(buffer_key: str) -> None:
    st.session_state[buffer_key] = st.session_state.get(buffer_key, "")[:-1]


def _clear_math(buffer_key: str) -> None:
    st.session_state[buffer_key] = ""


def _key_row(keys, prefix: str, buffer_key: str, columns: int = 8) -> None:
    cols = st.columns(columns)
    for index, (label, value) in enumerate(keys):
        with cols[index % columns]:
            st.button(
                label,
                key=f"{prefix}_{buffer_key}_{index}",
                use_container_width=True,
                on_click=_append_math,
                args=(buffer_key, value),
            )


def render_math_editor(
    target_key: str,
    label: str,
    placeholder: str,
    send_label: str,
) -> str | None:
    """
    The ordinary text field is never changed by a keypad button.
    This prevents iPad/Safari from losing freshly typed text during reruns.
    Mathematical symbols are collected in a separate buffer and combined on send.
    """
    buffer_key = f"{target_key}_math"
    if buffer_key not in st.session_state:
        st.session_state[buffer_key] = ""

    st.markdown(f"### {label}")
    manual_text = st.text_area(
        label,
        key=target_key,
        height=115,
        placeholder=placeholder,
        label_visibility="collapsed",
    )

    st.caption("Mathematische Ergänzung")
    math_buffer = st.text_input(
        "Mathematische Ergänzung",
        key=buffer_key,
        placeholder="Hier erscheinen Zeichen aus der Mathematik-Tastatur.",
        label_visibility="collapsed",
    )

    _key_row(QUICK_KEYS, "quick", buffer_key)
    _key_row(OPERATOR_KEYS, "operator", buffer_key)

    with st.expander("Weitere Zeichen und Formelvorlagen", expanded=False):
        sign_tab, builder_tab = st.tabs(("Zeichen", "Formel-Builder"))

        with sign_tab:
            _key_row(MORE_KEYS, "more", buffer_key, columns=4)

        with builder_tab:
            st.markdown("**Bruch**")
            c1, c2 = st.columns(2)
            with c1:
                numerator = st.text_input("Zähler", key=f"{target_key}_numerator")
            with c2:
                denominator = st.text_input("Nenner", key=f"{target_key}_denominator")
            if st.button(
                "Bruch einsetzen",
                key=f"{target_key}_fraction",
                use_container_width=True,
            ) and numerator.strip() and denominator.strip():
                _append_math(buffer_key, f"({numerator.strip()})/({denominator.strip()})")
                st.rerun()

            st.markdown("**Potenz**")
            c1, c2 = st.columns(2)
            with c1:
                base = st.text_input("Basis", key=f"{target_key}_base")
            with c2:
                exponent = st.text_input("Exponent", key=f"{target_key}_exponent")
            if st.button(
                "Potenz einsetzen",
                key=f"{target_key}_power",
                use_container_width=True,
            ) and base.strip() and exponent.strip():
                _append_math(buffer_key, f"({base.strip()})^({exponent.strip()})")
                st.rerun()

            st.markdown("**Wurzel**")
            root_value = st.text_input(
                "Ausdruck unter der Wurzel",
                key=f"{target_key}_root",
            )
            if st.button(
                "Wurzel einsetzen",
                key=f"{target_key}_root_button",
                use_container_width=True,
            ) and root_value.strip():
                _append_math(buffer_key, f"√({root_value.strip()})")
                st.rerun()

    combined = " ".join(
        part for part in (manual_text.strip(), math_buffer.strip()) if part
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
            disabled=not bool(combined),
            key=f"{target_key}_send",
        )
    with c2:
        st.button(
            "⌫ Mathe",
            use_container_width=True,
            disabled=not bool(math_buffer),
            key=f"{target_key}_delete_math",
            on_click=_delete_math,
            args=(buffer_key,),
        )
    with c3:
        st.button(
            "Mathe löschen",
            use_container_width=True,
            disabled=not bool(math_buffer),
            key=f"{target_key}_clear_math",
            on_click=_clear_math,
            args=(buffer_key,),
        )

    if send:
        return combined
    return None
