from langchain_ollama import OllamaLLM

researcher = OllamaLLM(model="llama3")
coder = OllamaLLM(model="qwen2.5:3b")

task = input("Task: ")

print("\nResearch Agent:\n")
print(researcher.invoke(task))

print("\nCode Agent:\n")
print(coder.invoke(task))
