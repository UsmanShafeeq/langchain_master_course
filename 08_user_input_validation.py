from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

while True:
    q = input("Ask a question: ").strip()
    if not q:
        print("Please enter a valid question.")
        continue

    if q == "exit":
        print("Exiting the program.")
        break
    print(llm.invoke(q))
