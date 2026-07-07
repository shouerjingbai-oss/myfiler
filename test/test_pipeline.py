"""
Test RAG Pipeline
"""

from pathlib import Path

from rag.manager import get_pipeline


PDF_PATH = Path("docs/test.pdf")


def main():

    pipeline = get_pipeline()

    print("=" * 60)
    print("Pipeline Test")
    print("=" * 60)

    pipeline.clear()

    chunks = pipeline.build(PDF_PATH)

    print(f"Chunks : {chunks}")

    docs = pipeline.search(
        "请输入一个你PDF里面存在的问题",
        top_k=3,
    )

    print(f"\nRetrieved {len(docs)} documents.\n")

    for i, doc in enumerate(docs, 1):

        print("-" * 60)

        print(f"Document {i}")

        print(doc.metadata)

        print(doc.page_content[:300])

    print("\nPipeline test passed!")


if __name__ == "__main__":
    main()
