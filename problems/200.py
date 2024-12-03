from collections import deque


def solve(grid):
    coords = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "1":
                coords.add((x, y))

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    islands = 0

    while coords:
        q = deque([coords.pop()])
        islands += 1

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                next_coord = (x + dx, y + dy)
                if next_coord in coords:
                    q.append(next_coord)
                    coords.remove(next_coord)

    return islands


if __name__ == "__main__":
    assert (
        solve(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        solve(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
