
def rev(x):
    sign = -1 if x < 0 else 1
    x = int(str(abs(x))[::-1])
    if x >= 0xffffffff:
        return 0
    return x * sign


assert rev(123) == 321
assert rev(-123) == -321
assert rev(120) == 21
assert rev(1534236469) == 0
