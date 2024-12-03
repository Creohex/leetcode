#!python
# Interval list intersections


def solve(l1: list, l2: list) -> list:
    ans = []
    p1 = 0
    p2 = 0

    while p1 < len(l1) and p2 < len(l2):
        (x1, y1), (x2, y2) = l1[p1], l2[p2]
        new_x, new_y = max(x1, x2), min(y1, y2)
        if new_y >= new_x:
            ans.append([new_x, new_y])
        if y1 <= y2:
            p1 += 1
        else:
            p2 += 1

    return ans


if __name__ == "__main__":
    assert solve(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
