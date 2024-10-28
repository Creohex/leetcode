from collections import deque

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


if __name__ == "__main__":
    assert solve_dfs(3, 5, 4) == True
    assert solve_bfs(3, 5, 4) == True
