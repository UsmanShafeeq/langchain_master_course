from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings

llm = OllamaLLM(model="llama3")
embeddings = OllamaEmbeddings(model="llama3")

db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

def get_context(query):
    docs = db.similarity_search(query, k=4)
    return "\n\n".join([d.page_content for d in docs])

while True:
    q = input("You: ")
    if q == "exit":
        break

    context = get_context(q)

    response = llm.invoke(f"""
You are an expert assistant.

Use context carefully:

Context:
{context}

Question:
{q}
""")

    print(response)