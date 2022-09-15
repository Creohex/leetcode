

def max_area(height):
    ## bruteforce:
    # from itertools import combinations
    # result = 0
    # for (i1, h1), (i2, h2) in combinations(enumerate(height), 2):
    #     result = max(result, (i2 - i1) * min(h1, h2))
    # return result

    i = 0
    j = len(height) - 1
    max_val = 0

    while i < j:
        cur = (j - i) * min(height[i], height[j])
        max_val = max(max_val, cur)

        if height[i] < height[j]:
            idx = i
            while i < j and height[idx] >= height[i]:
                i += 1
        elif height[i] >= height[j]:
            idx = j
            while i < j and height[idx] >= height[j]:
                j -= 1

    return max_val


assert max_area([1,8,6,2,5,4,8,3,7]) == 49
assert max_area([1,1]) == 1
assert max_area([4,3,2,1,4]) == 16
