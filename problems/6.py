
def convert(s, num_rows):
    if num_rows == 1:
        return s
    blocks = [""] * num_rows
    level = 0
    step = 1

    for c in s:
        blocks[level] += c
        level += step
        if level == num_rows - 1 and step > 0 or not level and step < num_rows:
            step *= -1

    return "".join(blocks)


"""
P   A   H   N
A P L S I I G
Y   I   R
"""
assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
"""
P     I    N
A   L S  I G
Y A   H R
P     I
"""
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("A", 1) == "A"
assert convert("AB", 1) == "AB"
