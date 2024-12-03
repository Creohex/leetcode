#!python


def solve(seq, target):
    l, r = 0, 0
    total = seq[0]
    min_range = 1 if total >= target else float("inf")

    while r < len(seq) and l < len(seq):
        if r == len(seq) - 1:
            if l == len(seq) - 1:
                break
            total -= seq[l]
            l += 1
        elif total <= target or l == r:
            r += 1
            total += seq[r]
        elif l < r:
            total -= seq[l]
            l += 1

        if total >= target:
            min_range = min(min_range, r - l + 1)

    return 0 if min_range == float("inf") else min_range


def solve(seq, target):
    l, r = 0, 0
    total = seq[0]
    min_range = float("inf")

    while r < len(seq):
        if total < target:
            r += 1
            if r < len(seq):
                total += seq[r]
        else:
            min_range = min(min_range, r - l + 1)
            total -= seq[l]
            l += 1

    return 0 if min_range == float("inf") else min_range


if __name__ == "__main__":
    assert solve([2, 3, 1, 2, 4, 3], 7) == 2
    assert solve([1, 4, 4], 4) == 1
    assert solve([1, 1, 1, 1, 1, 1, 1, 1], 11) == 0
    assert solve([10, 2, 3], 6) == 1
