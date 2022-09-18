
from functools import reduce


def from_roman(s):

    letters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    s = list(s[::-1])
    ans = 0

    while len(s):
        val = s.pop(0)

        while len(s) and letters[s[0]] < letters[val[0]]:
            val += s.pop(0)

        ans += (reduce(lambda a,b: letters[a] - letters[b], val)
                if len(val) > 1 else letters[val[0]])

    return ans


assert from_roman("III") == 3
assert from_roman("LVIII") == 58
assert from_roman("MCMXCIV") == 1994
