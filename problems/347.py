from heapq import nlargest, heappush
from collections import defaultdict, deque



def solve(nums: list, k):
    h = []
    for n in set(nums):
        heappush(h, (nums.count(n), n))
    return [v for _,v in nlargest(k, h)]

def solve2(nums: list, k):
    h = []
    nums = sorted(nums)
    print(nums)
    while nums:
        v = nums.pop(0)
        l = 1
        while nums and nums[0] == v:
            nums.pop(0)
            l += 1
        heappush(h, (l, v))
    ans = [b for a, b in nlargest(k, h, key=lambda t: t[0])]
    # print(ans)
    return ans

def solve3(nums: list, k):
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

    ans = []
    for _ in range(k):
        curr_max = max(d, key=d.get)
        ans.append(curr_max)
        del d[curr_max]

    # print(ans)
    return ans

if __name__ == "__main__":
    assert solve3([1, 1, 1, 1, 2, 2, 2, 3], k=2) == [1, 2]
    assert solve3([1], 1) == [1]
    assert solve3([4,1,-1,2,-1,2,3], 2) == [-1, 2]
