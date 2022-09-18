
def three_sum(nums):

    nums = sorted(nums)
    combinations = set()

    for i in range(len(nums) - 2):
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            val = nums[left] + nums[right]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                combinations.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1

    return combinations


def transform(l):
    return set(tuple(_) for _ in l)

assert three_sum([0,1,1]) == transform([])
assert three_sum([0,0,0]) == transform([[0,0,0]])
assert three_sum([-1,0,1,2,-1,-4]) == transform([[-1,-1,2],[-1,0,1]])
