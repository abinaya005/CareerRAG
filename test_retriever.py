import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="career_documents"
)

results = collection.get()

print("Number of documents:", len(results["documents"]))

for i, document in enumerate(results["documents"]):
    print("\n--- DOCUMENT", i + 1, "---")
    print(document)