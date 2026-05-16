from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3", streaming=True)

for chunk in llm.stream("Explain AI"):
    print(chunk, end="")
