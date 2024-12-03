#!python


def solve(nums):
    return max(map(len, "".join(map(str, nums)).split("0")))


def solve(nums):
    max_consequent = 0
    curr = 0

    for val in nums:
        if val == 1:
            curr += 1
        else:
            max_consequent = max(max_consequent, curr)
            curr = 0
    return max(max_consequent, curr)


if __name__ == "__main__":
    assert solve([1, 1, 0, 1, 1, 1]) == 3
