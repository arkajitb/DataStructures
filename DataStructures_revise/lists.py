# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.


nums = [1,0,1,1,0,1]

count = 0
result = 0
# if nums.count(1) is len(nums):
#     return len(nums)
# elif nums.count(1) is 0:
#     return 0

for i in range(len(nums)):
    if nums[i] is 1:
        count += 1
    else:
        
        result = max(result, count)
        
        count = 0
        

print('count', count, 'result', result)  
if (result >= count):
    print(result)
else:
    print(count)