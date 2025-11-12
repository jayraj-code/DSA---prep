class Solution:
    def max_sum_subarray(self, nums: list, k: int) -> int:
        n = len(nums)
        if n < k:
            return 0  # Cannot form a subarray of size k

        # 1. Initialization: Calculate the sum of the very first window (O(k))
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # 2. Slide the window one step at a time (O(N))
        #    'i' is the index of the element entering the window.
        for i in range(k, n):
            # 3. Update in O(1):
            #    A. Add the new element (entering at index i)
            #    B. Subtract the old element (leaving at index i - k)
            current_sum = current_sum + nums[i] - nums[i - k]

            # 4. Track: Update the maximum sum found so far
            max_sum = max(max_sum, current_sum)

        return max_sum


# Test Cases
c1 = Solution()
print(f"Max Sum 1: {c1.max_sum_subarray([3, 4, 5, 2, 10, 12, 14], 3)}")  # Expected: 36 (from 10, 12, 14)
print(f"Max Sum 2: {c1.max_sum_subarray([3, 4, 5, 2, 10, 12, 14, 18, 20], 4)}")  # Expected: 64 (from 12, 14, 18, 20)


class Solution:
    def max_sum_subarray(self, nums: list, k: int) -> int:
        n = len(nums)
        if n < k:
            return 0  # Safety check

        # STEP 1: Initialization (Calculate first window sum)
        # O(k) operation
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # STEP 2: Slide the window from the k-th index to the end (O(N) loop)
        # 'i' is the index of the element that is entering the window
        for i in range(k, n):
            # O(1) Update:
            # 1. Add the element entering the window (nums[i])
            # 2. Subtract the element leaving the window (nums[i - k])
            current_sum = current_sum + nums[i] - nums[i - k]

            # Track the maximum
            max_sum = max(max_sum, current_sum)

        return max_sum


# Test Cases
c1 = Solution()
print(c1.max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0], 4))  # Output: 18