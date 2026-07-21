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


def _append(value: str, target_key: str) -> None:
    st.session_state[target_key] = st.session_state.get(target_key, "") + value


def _delete(target_key: str) -> None:
    st.session_state[target_key] = st.session_state.get(target_key, "")[:-1]


def _clear(target_key: str) -> None:
    st.session_state[target_key] = ""


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


def _key_row(keys, prefix: str, target_key: str, columns: int = 8) -> None:
    cols = st.columns(columns)
    for index, (label, value) in enumerate(keys):
        with cols[index % columns]:
            st.button(
                label,
                key=f"{prefix}_{target_key}_{index}",
                use_container_width=True,
                on_click=_append,
                args=(value, target_key),
            )


def _insert_fraction(target_key: str) -> None:
    numerator = st.session_state.get(f"{target_key}_numerator", "").strip()
    denominator = st.session_state.get(f"{target_key}_denominator", "").strip()
    if numerator and denominator:
        _append(f"({numerator})/({denominator})", target_key)


def _insert_power(target_key: str) -> None:
    base = st.session_state.get(f"{target_key}_base", "").strip()
    exponent = st.session_state.get(f"{target_key}_exponent", "").strip()
    if base and exponent:
        _append(f"({base})^({exponent})", target_key)


def _insert_root(target_key: str) -> None:
    value = st.session_state.get(f"{target_key}_root", "").strip()
    if value:
        _append(f"√({value})", target_key)


def render_math_editor(
    target_key: str,
    label: str,
    placeholder: str,
    send_label: str,
) -> str | None:
    st.markdown(f"### {label}")
    st.text_area(
        label,
        key=target_key,
        height=105,
        placeholder=placeholder,
        label_visibility="collapsed",
    )

    _key_row(QUICK_KEYS, "quick", target_key)
    _key_row(OPERATOR_KEYS, "operator", target_key)

    with st.expander("Weitere Zeichen und Formelvorlagen", expanded=False):
        sign_tab, builder_tab = st.tabs(("Zeichen", "Formel-Builder"))

        with sign_tab:
            _key_row(MORE_KEYS, "more", target_key, columns=4)

        with builder_tab:
            st.markdown("**Bruch**")
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Zähler", key=f"{target_key}_numerator")
            with c2:
                st.text_input("Nenner", key=f"{target_key}_denominator")
            st.button(
                "Bruch einsetzen",
                key=f"{target_key}_fraction",
                use_container_width=True,
                on_click=_insert_fraction,
                args=(target_key,),
            )

            st.markdown("**Potenz**")
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Basis", key=f"{target_key}_base")
            with c2:
                st.text_input("Exponent", key=f"{target_key}_exponent")
            st.button(
                "Potenz einsetzen",
                key=f"{target_key}_power",
                use_container_width=True,
                on_click=_insert_power,
                args=(target_key,),
            )

            st.markdown("**Wurzel**")
            st.text_input("Ausdruck unter der Wurzel", key=f"{target_key}_root")
            st.button(
                "Wurzel einsetzen",
                key=f"{target_key}_root_button",
                use_container_width=True,
                on_click=_insert_root,
                args=(target_key,),
            )

    text = st.session_state.get(target_key, "").strip()
    if text:
        st.markdown("**Vorschau**")
        try:
            st.latex(readable_to_latex(text))
        except Exception:
            st.code(text)

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
        st.button(
            "⌫",
            use_container_width=True,
            disabled=not bool(text),
            key=f"{target_key}_delete",
            on_click=_delete,
            args=(target_key,),
        )
    with c3:
        st.button(
            "Löschen",
            use_container_width=True,
            disabled=not bool(text),
            key=f"{target_key}_clear",
            on_click=_clear,
            args=(target_key,),
        )

    if send:
        return text
    return None
