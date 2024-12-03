#!python

def solve(s: str, p: str) -> int:
    p_chars = {c: p.count(c) for c in set(p)}
    chars = {c: s[: len(p)].count(c) for c in p_chars}
    total_anagrams = [0] if all(chars[c] == n for c, n in p_chars.items()) else []

    for l in range(1, len(s) - len(p) + 1):

        r = l + len(p) - 1
        if s[r] in chars:
            chars[s[r]] += 1
        if s[l - 1] in chars:
            chars[s[l - 1]] -= 1
        if all(chars[c] == n for c, n in p_chars.items()):
            total_anagrams.append(l)

    print("ans: ", total_anagrams)
    return total_anagrams


if __name__ == "__main__":
    assert solve("cbaebabacd", "abc") == [0, 6]
    assert solve("abab", "ab") == [0, 1, 2]
    assert solve("baa", "aa") == [1]
