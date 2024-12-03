#!python


def solve(flowers, n):
    planted = 0
    flast = 0
    fnext = 0

    for i in range(len(flowers)):
        curr = flowers[i]
        flast = flowers[i - 1] if i > 0 else flast
        fnext = flowers[i + 1] if i < len(flowers) - 1 else fnext

        if all(map(lambda x: not bool(x), (curr, flast, fnext))):
            flowers[i] = 1
            planted += 1
            if planted >= n:
                return True

    return False


if __name__ == "__main__":
    assert solve([1, 0, 0, 0, 1], 1) == True
    assert solve([1, 0, 0, 0, 1], 2) == False
    assert solve([0], 1) == True
    assert solve([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 3) == True
    assert solve([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 4) == True
    assert solve([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 5) == False
