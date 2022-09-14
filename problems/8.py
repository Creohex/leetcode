import re

def atoi(s):
    f = re.match(r'\s*([-+]?)(\d+|\w+).*', s)

    try:
        val = int(f.group(2))
    except (ValueError, AttributeError):
        return 0

    ceil = 2 ** 31
    if val >= ceil:
        val = -ceil if f.group(1) == "-" else ceil - 1
    else:
        val = -val if f.group(1) == "-" else val

    return val


assert atoi("42") == 42
assert atoi("   -42") == -42
assert atoi("4193 with words") == 4193
assert atoi(".1") == 0
