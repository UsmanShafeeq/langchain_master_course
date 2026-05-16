from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

try:
    print(llm.invoke("Explain AI"))

except Exception as e:
    print(f"An error occurred: {e}")
