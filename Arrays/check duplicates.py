def check_duplicates(nums):
    return len(nums) != len(set(nums))

print(check_duplicates([1,2,3,4,5,6]))

