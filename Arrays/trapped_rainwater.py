def trap(height):
    if len(height) < 3:
        return 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    total = 0

    while left <= right:
        if left_max <= right_max:
            if height[left] < left_max:
                total += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if right_max > height[right]:
                total += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1


    return total

print(trap([1,2,3,4,5]))
print(trap([4,2,0,3,2,5,1,2,1,4]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))