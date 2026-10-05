from rag.loader import load_pdf

text = load_pdf("data/documents/resume.pdf")

print(text)
