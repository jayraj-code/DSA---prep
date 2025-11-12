from typing import List
class Solution:
    def moveZeroes(self, nums) :
        n = len(nums)
        insert_pos = 0

        for i in range(n):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1

        return nums

s1 = Solution()
print(s1.moveZeroes([0,1,0,3,12]))
print(s1.moveZeroes([0]))