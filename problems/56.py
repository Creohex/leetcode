def solve(intervals):
    intervals = sorted(intervals, key=lambda e: e[0])
    ans: list[list[int]] = [intervals[0]]

    for x2, y2 in intervals[1:]:
        curr = ans[-1]
        _, y1 = curr

        if y1 < x2:
            ans.append([x2, y2])
        else:
            curr[1] = max(y1, y2)

    return ans


if __name__ == "__main__":
    assert solve([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert solve([[1, 2], [3, 4], [4, 6]]) == [[1, 2], [3, 6]]
    assert solve([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solve([[1, 1000], [2, 5], [3, 7], [995, 999]]) == [[1, 1000]]
    assert solve([[1, 4], [0, 4]]) == [[0, 4]]
    assert solve([[1, 4], [5, 19], [0, 0]]) == [[0, 0], [1, 4], [5, 19]]
