
import statistics

def median(nums1, nums2):
    return statistics.median(nums1 + nums2)


assert median([1,3], [2]) == 2.0
assert median([1,2], [3,4]) == 2.5
assert median([1,3], [2,7]) == 2.5
