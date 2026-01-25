## 🦙 Ollama Python Projects

This repository contains simple Python examples for working with **Ollama locally**, including:
- Running LLMs from Python
- Creating and using **custom models** with Modelfiles

Official Ollama repo: https://github.com/ollama/ollama

---

### 0. Simple Python Client

This example shows how to call a local Ollama model from Python.

#### Prerequisites

1. Install Ollama on your machine  
   👉 https://ollama.com

2. Pull and run a model:
```bash
ollama run llama3.2:1b
```

3. Verify the Ollama server is running:
```bash
curl http://localhost:11434     # Ollama is running
```

4. Run the Python script:
```bash
python ollama_chat.py
```

---

### 1. Create a Custom Model using a Modelfile

You can create your own model by defining a **Modelfile**.

#### Step 1: Create a Modelfile
Create a file **without an extension**:

```bash
touch 1-ModelFile
```

Example `1-ModelFile`:
```text
FROM llama3.2:1b
SYSTEM You are a Linux command line expert.
```

---

#### Step 2: Build the model

```bash
ollama create LinuxAssistant -f ./ollama/1-ModelFile
```

---

#### Step 3: Run your custom model
```bash
ollama run LinuxAssistant
```

Now your assistant will always behave like a Linux expert 🐧

---

### References

- Ollama Modelfile docs:    https://docs.ollama.com/modelfile
- Ollama GitHub:    https://github.com/ollama/ollama