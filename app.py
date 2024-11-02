import os
import json
from datetime import datetime
import time
from flask import Flask, request, jsonify, render_template
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Set up Flask app
app = Flask(__name__)

# Define directories for persistence and document storage
PERSIST_DIRECTORY = r"C:\Users\cheru\OneDrive\Desktop\Q&A bot project NS\chroma_db"
PDF_FOLDER_PATH = r"C:\Users\cheru\OneDrive\Desktop\Q&A bot project NS\pdfs"

# Function to check if retraining is needed
def needs_retraining():
    if not os.path.exists(PERSIST_DIRECTORY):
        return True
    for filename in os.listdir(PDF_FOLDER_PATH):
        if filename.endswith(".pdf"):
            file_path = os.path.join(PDF_FOLDER_PATH, filename)
            if os.path.getmtime(file_path) > os.path.getmtime(PERSIST_DIRECTORY):
                return True
    return False

# Load or create vector store
def load_or_create_vector_store():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/msmarco-distilbert-base-v4")

    if needs_retraining():
        print("Training Chroma database from scratch...")
        loader = DirectoryLoader(PDF_FOLDER_PATH, loader_cls=PyPDFLoader)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_documents(documents)
        for document in texts:
            document.metadata["source"] = document.metadata.get("source", "Unknown Source")
        vector_store = Chroma.from_documents(texts, embedding=embedding, persist_directory=PERSIST_DIRECTORY)
        vector_store.persist()
    else:
        print("Loading existing Chroma database.")
        vector_store = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embedding)

    return vector_store

# Initialize the vector store and LLM with Groq API
try:
    vector_store = load_or_create_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatGroq(model="llama-3.2-3b-preview"),  # Adjust as per your model's name if necessary
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
except Exception as e:
    print("Error initializing vector store or LLM:", e)

# Function to process query and retrieve the answer along with source
def answer_query(query):
    try:
        print(f"User Question: {query}")
        llm_response = qa_chain(query)
        answer_text = llm_response['result']
        source_documents = llm_response.get("source_documents", [])
        source = source_documents[0].metadata.get("source", "Unknown Source") if source_documents else "Unknown Source"
        result = {"answer": answer_text, "source": source}
        print(result)
        return result
    except Exception as e:
        print("Error during query processing:", e)
        return {"answer": "Error fetching response. Please try again.", "source": "Unknown Source"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('user_input')
    if user_input:
        response = answer_query(user_input)
        return jsonify(response)
    else:
        return jsonify({"answer": "Error: No input received"}), 400

if __name__ == '__main__':
    print("Starting the Q&A Chatbot...")
    app.run(debug=True, host="127.0.0.1", port=5000)
