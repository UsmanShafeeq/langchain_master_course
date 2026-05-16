from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3")
texts = [
    "AI is used in healthcare",
    "Machine learning is part of AI",
    "Deep learning uses neural networks",
    "Python is widely used in AI development",
]

vector_db = Chroma.from_texts(
    texts=texts, embedding=embeddings, persist_directory="chroma_db"
)

print("Vector database created successfully ")
