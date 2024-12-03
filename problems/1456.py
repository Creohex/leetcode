#!python


def solve(word, k):
    vowels = set("aeiou")
    longest_substring = 0
    current = 0

    for r in range(len(word)):
        l = r - k
        if word[r] in vowels:
            current += 1
        if l >= 0:
            current -= 1 if word[l] in vowels else 0
        longest_substring = max(longest_substring, current)

    return longest_substring


if __name__ == "__main__":
    assert solve("abciiidef", 3) == 3
    assert solve("aeiou", 2) == 2
    assert solve("leetcode", 3) == 2
