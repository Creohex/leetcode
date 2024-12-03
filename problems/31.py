#!python


# Logic:
#   1. Find 'pivot': last part in non-decreasing (increasing or equal) order, left element of the pair
#   2. Find right-most element greater than pivot
#   3. Switch pivot and right-most element
#   4. Reverse everything after the pivot


def next_permutation(nums):
    i = len(nums) - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1 :] = reversed(nums[i + 1 :])

    # print("ans: ", nums)
    return nums


if __name__ == "__main__":
    assert next_permutation([1, 2, 3]) == [1, 3, 2]
    assert next_permutation([3, 2, 1]) == [1, 2, 3]
    assert next_permutation([1, 1, 5]) == [1, 5, 1]
    assert next_permutation([1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert next_permutation([1, 1, 1, 5, 1, 1, 1, 1]) == [1, 1, 5, 1, 1, 1, 1, 1]
    assert next_permutation([1, 1, 1, 5, 4, 3, 2, 1]) == [1, 1, 2, 1, 1, 3, 4, 5]
