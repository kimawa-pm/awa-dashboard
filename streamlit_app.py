import streamlit as st
from pathlib import Path

st.set_page_config(page_title="AWA Holdings Dashboard", layout="wide")

st.title("AWA Holdings Dashboard")

html_path = Path("index.html")
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=2200, scrolling=True)
