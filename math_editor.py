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


def _apply_pending_change(target_key: str) -> None:
    """Apply keyboard changes before the text-area widget is created."""
    pending_key = f"{target_key}_pending_value"
    if pending_key in st.session_state:
        st.session_state[target_key] = st.session_state.pop(pending_key)


def _queue_value(target_key: str, value: str) -> None:
    """Store a new value for the next Streamlit run."""
    st.session_state[f"{target_key}_pending_value"] = value
    st.rerun()


def _render_key_row(
    keys: tuple[tuple[str, str], ...],
    prefix: str,
    target_key: str,
    current_text: str,
    columns: int = 8,
) -> None:
    cols = st.columns(columns)
    for index, (label, value) in enumerate(keys):
        with cols[index % columns]:
            if st.button(
                label,
                key=f"{prefix}_{target_key}_{index}",
                use_container_width=True,
            ):
                # Use the value returned by the text area in this exact run.
                # This preserves freshly typed text on iPad before adding a symbol.
                _queue_value(target_key, current_text + value)


def render_math_editor(
    target_key: str,
    label: str,
    placeholder: str,
    send_label: str,
) -> str | None:
    _apply_pending_change(target_key)

    st.markdown(f"### {label}")
    current_text = st.text_area(
        label,
        key=target_key,
        height=105,
        placeholder=placeholder,
        label_visibility="collapsed",
    )

    _render_key_row(QUICK_KEYS, "quick", target_key, current_text)
    _render_key_row(OPERATOR_KEYS, "operator", target_key, current_text)

    with st.expander("Weitere Zeichen und Formelvorlagen", expanded=False):
        sign_tab, builder_tab = st.tabs(("Zeichen", "Formel-Builder"))

        with sign_tab:
            _render_key_row(
                MORE_KEYS,
                "more",
                target_key,
                current_text,
                columns=4,
            )

        with builder_tab:
            st.markdown("**Bruch**")
            c1, c2 = st.columns(2)
            with c1:
                numerator = st.text_input(
                    "Zähler",
                    key=f"{target_key}_numerator",
                )
            with c2:
                denominator = st.text_input(
                    "Nenner",
                    key=f"{target_key}_denominator",
                )
            if st.button(
                "Bruch einsetzen",
                key=f"{target_key}_fraction",
                use_container_width=True,
            ):
                if numerator.strip() and denominator.strip():
                    _queue_value(
                        target_key,
                        current_text + f"({numerator.strip()})/({denominator.strip()})",
                    )

            st.markdown("**Potenz**")
            c1, c2 = st.columns(2)
            with c1:
                base = st.text_input(
                    "Basis",
                    key=f"{target_key}_base",
                )
            with c2:
                exponent = st.text_input(
                    "Exponent",
                    key=f"{target_key}_exponent",
                )
            if st.button(
                "Potenz einsetzen",
                key=f"{target_key}_power",
                use_container_width=True,
            ):
                if base.strip() and exponent.strip():
                    _queue_value(
                        target_key,
                        current_text + f"({base.strip()})^({exponent.strip()})",
                    )

            st.markdown("**Wurzel**")
            root_value = st.text_input(
                "Ausdruck unter der Wurzel",
                key=f"{target_key}_root",
            )
            if st.button(
                "Wurzel einsetzen",
                key=f"{target_key}_root_button",
                use_container_width=True,
            ):
                if root_value.strip():
                    _queue_value(
                        target_key,
                        current_text + f"√({root_value.strip()})",
                    )

    text = current_text.strip()
    if text:
        st.markdown("**Vorschau**")
        math_symbols = set("=+-−·×:÷√^²³()[]/%παβγΔ≤≥≠")
        symbol_count = sum(1 for char in text if char in math_symbols)
        word_count = len(text.split())
        looks_mathematical = symbol_count >= 1 and word_count <= 8

        if looks_mathematical:
            try:
                st.latex(readable_to_latex(text))
            except Exception:
                st.code(text)
        else:
            st.markdown(text)

    c1, c2, c3 = st.columns(3)
    with c1:
        send = st.button(
            send_label,
            type="primary",
            use_container_width=True,
            disabled=not bool(text),
            key=f"{target_key}_send",
        )
    with c2:
        if st.button(
            "⌫",
            use_container_width=True,
            disabled=not bool(current_text),
            key=f"{target_key}_delete",
        ):
            _queue_value(target_key, current_text[:-1])
    with c3:
        if st.button(
            "Löschen",
            use_container_width=True,
            disabled=not bool(current_text),
            key=f"{target_key}_clear",
        ):
            _queue_value(target_key, "")

    if send:
        return current_text.strip()
    return None
