import ollama

"""
    Demonstrate how to use the Ollama Python client to interact with both raw text prediction models
    Make sure that ollma server is running locally
    Select the model you want to use

"""

model = "llama3.2:1b"       # Change to your desired model name
client = ollama.Client()    

def raw_model_api():
    
    # API - /api/generate for raw (text prediction) models
    response = client.generate(model=model, prompt="Explain Python")
    print(response.response)


def chat_model_api():
    
    # API - /api/chat for conversational models
    response = client.chat(
        model=model, 
        messages=[
            { "role": "system", "content": "You are a Linux expert" },
            { "role": "user", "content": "Explain Kubernetes" }
        ], 
        stream=False
        )
    print(response["message"]['content'])



def main():
    try: 
        raw_model_api()
        chat_model_api()
    except Exception as e:
        print(f"An error occurred: {e}")    


if __name__ == "__main__":
    main()