def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for i in range (len(nums)):
        if nums[i] == 1:
            count += 1
            max_count = max(max_count , count)

        else :
            count = 0
    return max_count

print(max_consecutive_ones([1,1,1,0,2,1,1,1,1]))


nums = [1,1,0,1,1,1]

step1 = list(map(str, nums))
print(step1)  # ['1', '1', '0', '1', '1', '1']

step2 = ''.join(step1)
print(step2)  # "110111"

step3 = step2.split('0')
print(step3)  # ['11', '111']

step4 = list(map(len, step3))
print(step4)  # [2, 3]

result = max(step4)
print(result)  # 3
