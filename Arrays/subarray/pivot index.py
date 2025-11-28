def PivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        # Right sum = total - left - current element
        right_sum = total_sum - left_sum - nums[i]

        if left_sum == right_sum:
            return i

        # Add current element to left sum for next iteration
        left_sum += nums[i]

    return -1


print(PivotIndex([1, 7, 3, 6, 5, 6]))  # 3
print(PivotIndex([1, 2, 3]))  # -1
print(PivotIndex([2, 1, -1]))  # 0
print(PivotIndex([-1, -1, -1, -1, -1, -1]))  # -1