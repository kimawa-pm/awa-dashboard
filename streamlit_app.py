import streamlit as st
from pathlib import Path

# FULL WIDTH + sin padding
st.set_page_config(layout="wide")

st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
iframe {
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

# Cargar HTML
html_path = Path("index.html")
html_content = html_path.read_text(encoding="utf-8")

# Mostrarlo más grande
st.components.v1.html(html_content, height=3000, scrolling=True)
