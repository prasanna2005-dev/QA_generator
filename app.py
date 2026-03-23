import streamlit as st
from rag import create_vector_db, retrieve_docs, generate_answer

st.set_page_config(page_title="RAG System")

st.title("📄 AI Document Q&A System")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
query = st.text_input("Ask a question from the document")

if uploaded_file and query:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing document...")

    db = create_vector_db("temp.pdf")
    docs = retrieve_docs(db, query)
    answer = generate_answer(query, docs)

    st.success("Answer generated!")

    st.subheader("📌 Answer")
    st.write(answer)

    st.subheader("📄 Retrieved Context")
    for i, doc in enumerate(docs):
        st.write(f"Chunk {i+1}:")
        st.write(doc.page_content)