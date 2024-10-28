from collections import deque
import math

def solve_dfs(x, y, target):
    seen = set()

    def dfs(v):
        if v == target:
            return True
        if v in seen or v < 0 or v > x + y:
            return False
        seen.add(v)

        return dfs(v - x) or dfs(v + x) or dfs(v - y) or dfs(v + y)

    return dfs(0)

def solve_bfs(x, y, target):
    q = deque([0])
    seen = set()
    directions = [x, -x, y, -y]

    while q:
        v = q.popleft()
        for dir in directions:
            new_v = v + dir
            if new_v == target:
                return True
            if new_v not in seen and 0 <= new_v <= x + y:
                seen.add(v)
                q.append(new_v)
    return False

def solve_bfs2(x, y, target):
    q = deque([(0, 0)])
    seen = set()

    def enqueue(a, b):
        if (a, b) not in seen:
            q.append((a, b))

    while q:
        a, b = q.popleft()
        if (a, b) in seen or a < 0 or b < 0 or a > x or b > y:
            continue
        if a + b == target:
            return True
        seen.add((a, b))

        enqueue(0, b)
        enqueue(a, 0)
        enqueue(x, b)
        enqueue(a, y)

        diff1 = min(y - b, a - b)
        enqueue(a - diff1, b + diff1)

        diff2 = min(x - a, b - a)
        enqueue(a + diff2, b - diff2)


    return False

if __name__ == "__main__":
    # assert solve_dfs(3, 5, 4) == True
    # assert solve_dfs(6, 7, 20) == False
    assert solve_bfs2(3, 5, 4) == True
    assert solve_bfs2(6, 7, 20) == False
    assert solve_bfs2(1, 2, 3) == True
