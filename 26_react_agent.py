from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

print("ReAct Agent Started")

while True:
    q = input("You: ")

    if q == "exit":
        break

    prompt = f"""
Think step by step and solve:

Question: {q}
"""

    print(llm.invoke(prompt))
