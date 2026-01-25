from fastapi import FastAPI
import chromadb
import ollama
import os
import logging


"""
    Build RAG API with FastAPI using Ollama and ChromaDB

        Make sure that ollama server is running locally
    Select the model you want to use by setting the OLLAMA_MODEL environment variable
    Add data to ChromaDB using /add endpoint
    Ask questions using /query endpoint
    Additional health check endpoint /health
"""

# Configuration and Initialization
app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

logging.basicConfig (       # Logging configuration
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

MODEL_NAME = os.getenv("OLLAMA_MODEL", "tinyllama")     # Default model is tinyllama
logging.info(f"Using Ollama model: {MODEL_NAME}")       


# API Endpoint /query to get answers 
@app.post("/query")
def query(q: str):
    """"
    Handle a query by retrieving relevant context from ChromaDB and generating an answer using Ollama.
    """
    logging.info(f"/query method: getting response for {q}")

    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama.generate(
        model=MODEL_NAME,
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}


# API Endpoint /add to add new data
@app.post("/add")
def add_data_chromadb(id: str, newdata: str) -> str:
    """
    Add new data to ChromaDB with the specified ID.
    """

    logging.info(f"/add method: adding data {newdata} with ID {id} into ChromaDB")
    if id is None or newdata is None:
        return {"error": "Both 'id' and 'newdata' parameters are required."}

    collection.add(documents=[newdata], ids=[id])

    return newdata + "is added to ChromaDB"
    print("New Embedding stored in Chroma")


@app.get("/health")
def health():
    logging.info(f"/health method: Checking health status")
    return {"status": "OK"}
