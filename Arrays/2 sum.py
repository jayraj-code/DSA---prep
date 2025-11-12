def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Found! Return indices (remember to adjust for 1-based indexing if needed)
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need a bigger sum: move the left pointer
            left += 1
        else:
            # Need a smaller sum: move the right pointer
            right -= 1

    return []  # No solution found

print(two_sum_sorted([1,2,3,4,6,8], 22))
print(two_sum_sorted([1,2,3,4,6,8], 12))
print(two_sum_sorted([1,2,3,4,6,8],3 ))