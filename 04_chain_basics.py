from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template("Give 3 point about  {topic}")

chain = prompt | llm

print(chain.invoke({"topic": "Cybersecurity"}))
