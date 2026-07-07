embedding = get_embedding_model()

vector = embedding.embed_query(
    "什么是人工智能？"
)

print(len(vector))
