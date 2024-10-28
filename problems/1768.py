import operator
from itertools import starmap, zip_longest


def solve(word1, word2):
    return "".join(starmap(operator.add, zip_longest(word1, word2, fillvalue="")))


if __name__ == "__main__":
    assert solve("abc", "def") == "adbecf"
    assert solve("", "def") == "def"
    assert solve("abc", "d") == "adbc"
