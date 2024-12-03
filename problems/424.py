#!python


from collections import defaultdict


def solve(s, k):
        unique_chars = defaultdict(int)
        l, r = 0, 0
        max_freq = 0
        max_length = 0

        for r in range(len(s)):
            unique_chars[s[r]] += 1
            max_freq = max(max_freq, unique_chars[s[r]])

            if r - l + 1 - max_freq > k:
                unique_chars[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        # print("ans: ", max_length)
        return max_length

if __name__ == "__main__":
    assert solve("ABAB", 2) == 4
    assert solve("AABABBA", 1) == 4
