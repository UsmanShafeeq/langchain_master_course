from langchain_ollama import OllamaLLM

model = input("Enter model (llama3/phi3/qwen2.5): ")

llm = OllamaLLM(model=model)

print(llm.invoke("Explain Machine Learning"))
