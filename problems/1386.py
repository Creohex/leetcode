#!python
# Cinema seats allocation

from collections import defaultdict


def solve(seats: list[list[int]], n: int) -> int:
    rows = defaultdict(set)
    for row, seat in seats:
        rows[row].add(seat)
    families = 0

    spots_left = set(range(2, 6))
    spots_right = set(range(6, 10))
    spots_inner = set(range(4, 8))

    for seats in rows.values():
        side_spots = False
        if not spots_left.intersection(seats):
            families += 1
            side_spots = True
        if not spots_right.intersection(seats):
            families += 1
            side_spots = True
        if not side_spots and not spots_inner.intersection(seats):
            families += 1

    return 2 * (n - len(rows)) + families


if __name__ == "__main__":
    assert solve([[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]], 3) == 4
