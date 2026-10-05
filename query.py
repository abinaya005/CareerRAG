from rag.embeddings import model
from rag.retriever import retrieve
from rag.llm import generate_answer

question = input("Ask a question about the resume: ")

query_embedding = model.encode(question)

results = retrieve(query_embedding)

context = "\n\n".join(results)

answer = generate_answer(context, question)

print("\nAnswer:")
print(answer)