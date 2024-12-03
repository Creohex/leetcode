#!python
# reverse words in a string


def solve(sentence: str) -> str:
    return " ".join(reversed(sentence.strip().split()))


if __name__ == "__main__":
    assert solve("the sky is blue") == "blue is sky the"
    assert solve("  hello world  ") == "world hello"
