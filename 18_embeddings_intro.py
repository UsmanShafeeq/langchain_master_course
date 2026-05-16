from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3")

text = "Machine learning helps computers learn from data"
vector = embeddings.embed_query(text)
print("Vector length:", len(vector))
print("\nFirst 10 values:", vector[:10])
