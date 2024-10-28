

import string

"""
split pattern in blocks
(letter or letter+modifier)
letter can be any (.)

for each pattern block -> iterate over input and check if it complies
"""
def is_match(s, p):

        characters = string.ascii_lowercase + "."
        i = 0
        blocks = []

        while True:
            if i >= len(p):
                break
            char = None

            if p[i] in characters:
                char = p[i]
            else:
                return False

            if i + 1 < len(p):
                if p[i + 1] == "*":
                    blocks.append((char, True))
                    i += 2
                else:
                    blocks.append((char, False))
                    i += 1
            else:
                blocks.append((char, False))
                break

        print(blocks)

        for i, block in enumerate(blocks):
            char, unlimited = block
            print(">", i, char, unlimited)
            if unlimited:
                while True:
                    if not s:
                        break
                    if char == ".":
                        next_block = None
                        if i + 1 < len(blocks):
                            next_block = blocks[i + 1]

                        if next_block:
                            if s[0] != next_block[0]:
                                s = s[1:]
                            else:
                                break
                        else:
                            return True
                    elif s[0] == char:
                        s = s[1:]
                    else:
                        break
            else:
                if not s:
                    break
                if s[0] == char:
                    s = s[1:]
                else:
                    return False
            print("\t", s)

        return not s


# assert is_match("aa", "a") is False
# assert is_match("aa", "a*") is True
# assert is_match("ab", ".*") is True
assert is_match("ab", ".*c") is False
# assert is_match("aab", "c*a*b") is True
