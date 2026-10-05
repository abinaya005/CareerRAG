from rag.llm import generate_answer

context = """
Abinaya knows Python and Java.
She has completed a B.E. in Computer Science and Engineering.
"""

question = "What programming languages does Abinaya know?"

answer = generate_answer(context, question)

print("Question:", question)
print("\nAnswer:", answer)