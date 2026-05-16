from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

history = []

print("ChatGPT Clone Started ")

while True:
    q = input("You: ")

    if q == "exit":
        break

    history.append("User: " + q)

    context = "\n".join(history[-6:])

    response = llm.invoke(context)

    history.append("AI: " + response)

    print("\nAI:", response)
