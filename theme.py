from __future__ import annotations

import streamlit as st


def inject_theme() -> None:
    st.markdown(
        """
        <style>
        .block-container {max-width: 980px; padding-top: 1.25rem;}
        .hero {
            border: 1px solid rgba(128,128,128,.20);
            border-radius: 20px;
            padding: 1.25rem 1.4rem;
            margin-bottom: 1rem;
        }
        .hero h1 {margin: 0;}
        div[data-testid="stButton"] button {min-height: 2.7rem;}
        div[data-testid="stTextArea"] textarea {font-size: 1.08rem;}
        </style>
        """,
        unsafe_allow_html=True,
    )
