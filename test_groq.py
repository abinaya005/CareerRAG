import os
from groq import Groq

api_key = os.environ.get("GROQ_API_KEY")

print("API key loaded:", bool(api_key))

client = Groq(api_key=api_key)

models = client.models.list()

print("Groq connection successful!")
print("Number of models:", len(models.data))