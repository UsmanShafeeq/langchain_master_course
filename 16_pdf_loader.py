from langchain_community.document_loaders import PyPDFLoader

file_path = "sample.pdf"

loader = PyPDFLoader(file_path)

documents = loader.load()

print("Total pages loaded:", len(documents))

print("\n--- First Page Preview ---\n")
print(documents[0].page_content[:1000])