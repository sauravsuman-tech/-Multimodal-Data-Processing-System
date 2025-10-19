import streamlit as st
import requests

API = "http://localhost:8000"

st.title("Multimodal Data Processing System")

st.header("Upload files")
uploaded = st.file_uploader("Choose files", accept_multiple_files=True)
if st.button("Upload"):
    files = []
    for f in uploaded:
        files.append(("files", (f.name, f.getvalue(), f.type)))
    resp = requests.post(f"{API}/upload/", files=files)
    st.write(resp.json())

st.header("Ask a question")
q = st.text_input("Question")
use_g = st.checkbox("Use Gemini (if available)", value=False)
k = st.slider("how many results to fetch", 1, 10, 5)
if st.button("Ask"):
    resp = requests.post(f"{API}/query/", data={"q": q, "use_gemini": str(use_g).lower(), "k": k})
    st.write(resp.json())