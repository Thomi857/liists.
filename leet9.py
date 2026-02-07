nums = [1,12,34,56,78]
def differenceOfSum(nums):
    elements_sum = sum(nums)
    digit_sum = 0
    for i in nums:  
        digit_sum += sum(int(digit) for digit in str(i))
    return elements_sum - digit_sum
print(differenceOfSum(nums))