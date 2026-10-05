from rag.loader import load_pdf
from rag.splitter import split_text
from rag.embeddings import create_embeddings

text = load_pdf("data/documents/resume.pdf")

chunks = split_text(text)

embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])