def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return nums[start:end + 1], max_sum


result, total = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(f"Subarray: {result}, Sum: {total}")

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range (1, len(nums)):
            current_sum = max(nums[i] , current_sum + nums[i])
            max_sum = max(current_sum , max_sum)
        return max_sum
c1 = Solution()
c1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
c1.maxSubArray([1])
c1.maxSubArray([5,4,-1,7,8])

