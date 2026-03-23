from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_TOKEN")
# Initialize LLM
llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

# Create Vector DB
def create_vector_db(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        
    )

    db = FAISS.from_documents(docs, embeddings)

    return db

# Retrieve relevant docs
def retrieve_docs(db, query):
    return db.similarity_search(query, k=3)

# Generate answer
def generate_answer(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}

Also mention relevant clauses or lines from the document.
"""

    response = llm.invoke(prompt)
    return response.content