

def longest_substring(s):

    longest = 0

    if len(s) <= 1:
        return len(s)

    for i in range(len(s)):
        count = 1
        used_local = set()

        for j in range(i + 1, len(s)):
            if s[j] in used_local or s[j] == s[i]:
                longest = max(longest, count)
                break
            count += 1
            used_local.add(s[j])
        else:
            longest = max(longest, count)

    return longest


assert longest_substring("abcabcbbd") == 3
assert longest_substring("bbbbb") == 1
assert longest_substring("pwwkew") == 3
assert longest_substring(" ") == 1
assert longest_substring("au") == 2
assert longest_substring("aab") == 2
