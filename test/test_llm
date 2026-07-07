"""
Test DeepSeek LLM
"""

from llm.client import get_llm


def main():

    llm = get_llm()

    print("=" * 60)
    print("LLM Test")
    print("=" * 60)

    response = llm.invoke("请用一句话介绍Transformer。")

    print(response.content)

    print("\nLLM test passed!")


if __name__ == "__main__":
    main()
