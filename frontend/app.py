import streamlit as st
import requests

st.title("RAG Chat")

query = st.text_input("Ask something")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        res = requests.get(
            "http://backend:8000/query",
            params={"q": query}
        )
        st.write(res.json()["answer"])
