from __future__ import annotations

import streamlit as st

from formula_library import CATEGORIES, formulas_for


def _copy_formula(display: str, target_key: str) -> None:
    st.session_state[target_key] = display


def render_formula_sidebar(topic_key: str, target_key: str) -> None:
    st.subheader("📚 Formelsammlung")
    category = st.selectbox("Bereich", CATEGORIES, key="formula_category")

    formulas = formulas_for(category, topic_key)
    for index, formula in enumerate(formulas):
        with st.container(border=True):
            st.markdown(f"**{formula.title}**")
            st.markdown(f"### {formula.display}")
            st.caption(formula.explanation)
            st.button(
                "In Eingabe übernehmen",
                key=f"formula_{category}_{index}",
                use_container_width=True,
                on_click=_copy_formula,
                args=(formula.display, target_key),
            )
