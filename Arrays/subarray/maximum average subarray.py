from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        max_start = 0
        for i in range (k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
                max_start = i-k+1
        best_window = nums[max_start : max_start + k]
        return max_sum/k , best_window

c1 = Solution()
print(c1.findMaxAverage([1,12,-5,-6,50,3], k = 4))