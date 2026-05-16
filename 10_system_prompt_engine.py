from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template("""
You are a strict AI teacher.

Question: {q}
""")

chain = prompt | llm

print(chain.invoke({"q": "What is Python?"}))
