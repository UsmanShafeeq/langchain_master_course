from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings

llm = OllamaLLM(model="llama3")
embeddings = OllamaEmbeddings(model="llama3")

db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

print("RAG Chatbot Started ")

while True:
    q = input("You: ")

    if q == "exit":
        break

    docs = db.similarity_search(q, k=3)
    context = "\n".join([d.page_content for d in docs])

    response = llm.invoke(f"""
Answer using context only:

{context}

Question: {q}
""")

    print(response)
