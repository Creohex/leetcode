
from itertools import permutations

def letter_combinations(digits):
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        letter_sets = [mapping[digit] for digit in digits]
        result = set()
        print(">", letter_sets)

        for ids in set(permutations(list(range(4)) * 2, r=len(digits))):
            word = ""
            for i, id in enumerate(ids):
                try:
                    word += letter_sets[i][id]
                except IndexError:
                    word = ""
                    break
            if word:
                result.add(word)

        print(result)
        return result


assert letter_combinations("234") == set([
    "adg","adh","adi","aeg","aeh","aei","afg", "afh","afi","bdg","bdh","bdi","beg",
    "beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])
assert letter_combinations("23") == set(["ad","ae","af","bd","be","bf","cd","ce","cf"])
assert letter_combinations("") == set()
assert letter_combinations("2") == set(["a","b","c"])
