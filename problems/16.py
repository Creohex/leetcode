
def three_sum_closest(nums, target):

        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum <= target:
                    left += 1
                else:
                    right -= 1

                if abs(closest - target) > abs(sum - target):
                    closest = sum

        return closest


assert three_sum_closest([-1,2,1,-4], 1) == 2
assert three_sum_closest([0,0,0], 1) == 0
assert three_sum_closest([1,1,1,1], 100) == 3
