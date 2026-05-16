from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3")
embeddings = OllamaEmbeddings(model="llama3")

db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)


def retrieve(query):
    docs = db.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])


prompt = ChatPromptTemplate.from_template("""
Context:
{context}

Question:
{question}
""")

chain = prompt | llm

while True:
    q = input("You: ")
    if q == "exit":
        break

    context = retrieve(q)

    print(chain.invoke({"context": context, "question": q}))
