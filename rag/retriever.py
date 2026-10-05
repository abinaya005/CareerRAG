import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="career_documents"
)

def retrieve(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results["documents"][0]