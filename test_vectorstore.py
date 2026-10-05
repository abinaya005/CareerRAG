from rag.loader import load_pdf
from rag.splitter import split_text
from rag.embeddings import create_embeddings
from rag.vectorstore import store_documents

text = load_pdf("data/documents/resume.pdf")

chunks = split_text(text)

embeddings = create_embeddings(chunks)

store_documents(chunks, embeddings)

print("Documents stored successfully!")
print("Number of chunks stored:", len(chunks))