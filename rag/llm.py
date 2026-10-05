from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def generate_answer(context, question):

    prompt = f"""
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content