"""
Test Embedding Model
"""

from models.embedding import get_embedding_model


def main():

    embedding = get_embedding_model()

    text = "什么是人工智能？"

    vector = embedding.embed_query(text)

    print("=" * 60)
    print("Embedding Test")
    print("=" * 60)

    print(f"Input : {text}")
    print(f"Dimension : {len(vector)}")
    print(f"First 10 values :")

    print(vector[:10])

    print("\nEmbedding test passed!")


if __name__ == "__main__":
    main()
