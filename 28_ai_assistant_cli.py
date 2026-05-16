from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

print("AI Assistant CLI Started ")

while True:
    q = input("You: ")

    if q in ["exit", "quit"]:
        break

    if q.startswith("/calc"):
        print(eval(q.replace("/calc", "")))
        continue

    print(llm.invoke(q))
