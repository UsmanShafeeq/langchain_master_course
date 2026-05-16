from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

memory = []

while True:
    q = input("You: ")
    memory.append(q)

    response = llm.invoke("\n".join(memory))
    print(response)