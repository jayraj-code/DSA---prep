from typing import List
class Solution:
    def sumOddLengthSubarrays(self, nums : List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            current_sum = nums[i] + current_sum
            max_sum = max(current_sum  , max_sum)
        return max_sum

c1 = Solution()
print(c1.sumOddLengthSubarrays([1,2,3,4,5,6]))
