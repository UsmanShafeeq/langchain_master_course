from langchain_ollama import OllamaLLM


class ProductionAI:
    def __init__(self):
        self.llm = OllamaLLM(model="llama3")
        self.memory = []

    def run(self):
        print("Production AI System Started 🚀")

        while True:
            q = input("You: ")

            if q == "exit":
                break

            self.memory.append(q)

            context = "\n".join(self.memory[-10:])

            response = self.llm.invoke(context)

            self.memory.append(response)

            print("\nAI:", response)


app = ProductionAI()
app.run()
