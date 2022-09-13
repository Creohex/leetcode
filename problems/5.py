
from itertools import combinations


def longest_palindromic_substring(s):
        longest_palindrome = s[0]
        indexes = {}

        for i in range(len(s)):
            if s[i] in indexes:
                indexes[s[i]].append(i)
            else:
                indexes[s[i]] = [i]

        for idx in indexes.values():
            if len(idx) < 2:
                continue

            for a, b in combinations(idx, 2):
                if b - a < len(longest_palindrome):
                    continue
                for i in range(1, ((b - a) // 2) + 1):
                    if s[a + i] != s[b - i]:
                        break
                else:
                    if len(longest_palindrome) < b - a + 1:
                        longest_palindrome = s[a:b + 1]
        return longest_palindrome


assert longest_palindromic_substring("a") == "a"
assert longest_palindromic_substring("ac") == "a"
assert longest_palindromic_substring("aacabdkacaa") == "aca"
assert longest_palindromic_substring("cbbd") == "bb"
assert longest_palindromic_substring("bababadqwe") == "babab"
