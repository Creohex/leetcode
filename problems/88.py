import heapq
from collections import deque


def solve(nums1: list[int], m: int, nums2: list[int], n: int):
    heapq.heapify(nums1)
    for x in nums2:
        v_min = heapq.heappop(nums1)
        nums1.append(max(v_min, x))
    print(nums1)
    return sorted(nums1)


# def solve(nums1: list[int], m: int, nums2: list[int], n: int):
#     heapq.heapify(nums2)

#     if m == 0:
#         nums1[:] = nums2
#         return nums1

#     for i, v in enumerate(nums1):
#         if v == 0:
#             nums1[i] = heapq.heappop(nums2)
#         else:
#             nums1[i] = heapq.heappushpop(nums2, v)

#     print("ans: ", nums1)
#     return nums1


def solve(nums1: list[int], m: int, nums2: list[int], n: int):
    p1, p2 = m - 1, n - 1
    curr = m + n - 1

    while p1 != -1 and p2 != -1:
        if nums1[p1] > nums2[p2]:
            nums1[curr] = nums1[p1]
            p1 -= 1
        else:
            nums1[curr] = nums2[p2]
            p2 -= 1
        curr -= 1

    if p1 == -1:
        nums1[:curr+1] = nums2[:p2 + 1]

    print(nums1)
    return nums1

if __name__ == "__main__":
    assert solve([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert solve([1], 1, [], 0) == [1]
    assert solve([], 0, [1], 1) == [1]
    assert solve([2, 0], 1, [1], 1) == [1, 2]
    assert solve([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
