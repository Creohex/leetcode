#!python


def solve(seq: list[str]) -> list[str]:
    if not seq:
        return []

    repeating = 1
    prev = seq[0]
    compressed = []

    for i in range(1, len(seq)):
        char = seq[i]
        if char == prev:
            repeating += 1
        else:
            compressed.append(prev)
            if repeating > 1:
                compressed.append(str(repeating))
            prev = char
            repeating = 1

    compressed.append(prev)
    if repeating > 1:
        compressed.append(str(repeating))

    # print("ans: ", compressed)
    return compressed


if __name__ == "__main__":
    assert solve(["a", "a", "b", "b", "c", "c", "c"]) == ["a", "2", "b", "2", "c", "3"]

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
