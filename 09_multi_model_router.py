from langchain_ollama import OllamaLLM

models = {"fast": "phi3", "smart": "llama3", "code": "qwen2.5:3b"}

choice = input("Which model do you want to use? (fast/smart/code): ")

llm = OllamaLLM(model=models[choice], temperature=0)

print(llm.invoke("Explain AI"))
