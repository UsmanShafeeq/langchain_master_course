from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words")

chain = prompt | llm

print(chain.invoke({"topic": "quantum computing"}))
