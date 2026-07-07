"""
Run All Tests
"""

import subprocess
import sys


tests = [
    "tests/test_embedding.py",
    "tests/test_llm.py",
    "tests/test_pipeline.py",
]


def main():

    for test in tests:

        print("=" * 60)

        print(test)

        print("=" * 60)

        result = subprocess.run(
            [sys.executable, test]
        )

        if result.returncode != 0:

            print(f"\n{test} failed.")

            return

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()
