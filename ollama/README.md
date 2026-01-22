## Ollama Python projects

### 0 Simple Python client
    1. Install Ollama on local machine
    2. Run Ollama with the selected model ex: ollama run llama3.2:1b  
    3. Verify Ollama server is running, ex: curl localhost:11434
    4. Run the script
    Ollama model info: https://github.com/ollama/ollama


### 1 Create a custom Model using Model file
    1. Create a model file without extension (ex: 1-ModelFile)
    2. Create model (ex: LinuxAssistant) based on the above model file, 
        ```
        ollama create LinuxAssistant -f ./ollama/1-ModelFile 
        ```
    3. Run the newly created model
        ```
        ollama run LinuxAssistant
        ```
    4. Run the script
    
    Model File info: https://docs.ollama.com/modelfile

****
