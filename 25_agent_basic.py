from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

while True:
    q = input("You: ")

    if q == "exit":
        break

    if "calculate" in q:
        print(eval(q.replace("calculate", "")))
    else:
        print(llm.invoke(q))
