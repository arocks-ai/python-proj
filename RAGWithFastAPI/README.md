## RAG API with FastAPI
    1 Develop RAG API with FastAPI Application
    2 Docker
    3 Deploy into K8
    4 Github Actions workflows

    Reference - https://learn.nextwork.org/projects/ai-devops-api


---

### 1.RAG with FastAPI

#### RAG workflow:
![RAG Workflow](./images/1-RAG-API-WorkFlow.png)

```bash
 1 Receive question 
 2 Search knowledge base with Chroma 
 3 Get relevant context 
 4 Combine context + question 
 5 Send to Ollamas tinyllama
 6 Return AI-generated answer based on your documents

```

---   
#### Environment Setup
1. Run Ollama LLM Locally 
2. Setup python environment


```bash

# Install and run a model locally
ollama --version
ollama run tinyllama    # run ollama with the given model
curl localhost:11434    # message: Ollama is running

# python setup
python -version         # make sure verion >= 3.12
python -m venv .venv    # create virtual env
source .venv/bin/activate
# deactivate (once work is done)

# install the required packages
pip install fastapi uvicorn chromadb ollama
pip list | grep -E "fastapi|uvicorn|chromadb|ollama"

```

#### Build KB and create FastAPI instance using 
1. Run Ollama LLM Locally 
2. Setup python environment

```bash

# create embed.py   # Build KB in chroma DB by storing the information
# create app.py     # FastAPI webserver, app.py file with "app" FastAPI instance  

# run uvicorn server
uvicorn --version
uvicorn app:app --reload    # Start a FastAPI application using the Uvicorn ASGI server
```


---

#### Test the Application

```bash

# From CLI
curl -X POST "http://127.0.0.1:8000/query" -G --data-urlencode "q=What is Kubernetes?"

# From Swagger UI
Open your browser: http://127.0.0.1:8000/docs
Test the /query endpoint with "What is Kubernetes?"

```

