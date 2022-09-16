
def roman(x):
        ranks = [
            (100, "C", "D", "M"),
            (10, "X", "L", "C"),
            (1, "I", "V", "X"),
        ]

        res = "M" * (x // 1000)
        x = x % 1000

        for rank, single, half, dec in ranks:
            val = x // rank
            if val < 4:
                res += single * val
            elif val == 4:
                res += single + half
            elif 5 <= val < 9:
                res += half + single * (val - 5)
            elif val == 9:
                res += single + dec
            else:
                res += dec
            x = x % rank

        print(res)
        return res


assert roman(3) == "III"
assert roman(58) == "LVIII"
assert roman(1994) == "MCMXCIV"
