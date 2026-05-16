from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate

# =========================
# 1. MODEL + EMBEDDINGS
# =========================

llm = OllamaLLM(model="llama3")
embeddings = OllamaEmbeddings(model="llama3")

# =========================
# 2. LOAD VECTOR DB
# =========================

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# =========================
# 3. RETRIEVAL FUNCTION
# =========================

def retrieve_context(query):
    docs = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])

# =========================
# 4. PROMPT ENGINE
# =========================

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}
""")

chain = prompt | llm

# =========================
# 5. CHAT LOOP
# =========================

print("\nRAG AI Assistant Started (type exit to stop)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    context = retrieve_context(query)

    response = chain.invoke({
        "context": context,
        "question": query
    })

    print("\nAI Answer:")
    print(response)
    print("-" * 50)