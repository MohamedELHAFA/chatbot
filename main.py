
import streamlit as st
from rag_pipeline import build_rag_qa

st.set_page_config(page_title="Assistant BDNB", layout="wide")
st.title("🏠 Assistant BDNB RAG (Optimisé)")

qa_chain = build_rag_qa()

query = st.text_input("Posez votre question sur les bâtiments :", "")
if query:
    with st.spinner("Recherche des documents..."):
        result = qa_chain({"query": query})
    st.markdown("### 🧠 Réponse :")
    st.write(result["result"])
