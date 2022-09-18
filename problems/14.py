
def longest_common_prefix(strs):
    pref = ""
    min_s = min(strs)

    for i in range(len(min_s)):
        if all(s[i] == min_s[i] for s in strs):
            pref += min_s[i]
        else:
            break

    return pref


assert longest_common_prefix(["flower","flow","flight"]) == "fl"
assert longest_common_prefix(["dog","racecar","car"]) == ""
