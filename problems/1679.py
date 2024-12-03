#!python
# Max number of k-sum pairs


def solve(seq: list[int], k: int) -> int:
    seq.sort()
    l, r = 0, len(seq) - 1
    total_pairs = 0

    while l < r:
        curr = seq[l] + seq[r]

        if curr == k:
            total_pairs += 1
            l += 1
            r -= 1
        elif curr < k:
            l += 1
        else:
            r -= 1

    return total_pairs


if __name__ == "__main__":
    assert solve([1, 2, 3, 4], 5) == 2
    assert solve([3, 1, 3, 4, 3], 6) == 1


# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
