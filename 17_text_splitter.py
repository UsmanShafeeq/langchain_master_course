from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is transforming industries.
Machine Learning is a subset of AI.
Deep Learning is a subset of Machine Learning.
RAG systems combine retrieval and generation.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)
