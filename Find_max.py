def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            # (Fill in the missing line here)
            max_num = num
    return max_num

nums = (3,20,1)
print (find_max(nums))