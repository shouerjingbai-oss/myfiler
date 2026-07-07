"""
Test Agent
"""

from rag.manager import get_pipeline

from agent.agent_executor import create_agent


def main():

    pipeline = get_pipeline()

    if pipeline.size() == 0:

        print("Knowledge base is empty.")

        print("Please run test_pipeline.py first.")

        return

    agent = create_agent()

    print("=" * 60)
    print("Agent Test")
    print("=" * 60)

    while True:

        question = input("\nQuestion (exit to quit): ")

        if question.lower() == "exit":

            break

        result = agent.invoke(
            {
                "input": question,
            }
        )

        print("\nAnswer:\n")

        print(result["output"])


if __name__ == "__main__":
    main()
