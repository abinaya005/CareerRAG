from rag.loader import load_pdf
from rag.splitter import split_text

text = load_pdf("data/documents/resume.pdf")

chunks = split_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\n--- CHUNK", i + 1, "---")
    print(chunk)