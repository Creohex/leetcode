
from itertools import combinations

def two_sum(nums, target) -> list[int]:
    return next([i, j] for i, j in combinations(range(len(nums)), 2)
                if nums[i] + nums[j] == target)

def two_sum(nums, target) -> list[int]:
    s = {}
    for k, v in enumerate(nums):
        diff = target - v
        if diff in s:
            return [s[diff], k]
        s[v] = k

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
