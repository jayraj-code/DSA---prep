# Task: Complete the linear_search function
def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
    # Your code here: Find the index of the target
    # Return index if found, or -1 if not found.


# Test Case 1: Best Case (O(1))
print(linear_search([5, 12, 3, 8], 5))

# Test Case 2: Worst Case (O(N))
print(linear_search([5, 12, 3, 8], 8))

# Test Case 3: Target Absent (O(N))
print(linear_search([5, 12, 3, 8], 99))