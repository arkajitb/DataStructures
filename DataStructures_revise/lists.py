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

#--------------------------------------------------------------------
#Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_nums = 0
        
        
        
        for values in nums:
            values = str(values)
            if (len(values)%2 == 0):
                
                even_nums += 1
        return even_nums

#----------------------------------------------------------------------
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [x*x for x in A]
        A.sort()
        return A

#-------------------------------------------------------------------------
# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything from your function.

 

# Example 1:

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        
        i = 0
        while i < length:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i = i+2
            else:
                i = i + 1
            
        return arr
# #------------------------------------------------------------------------------
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if (len(nums1) == len(nums2)):
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            print(nums1)
        
        if len(nums2) is not 0:    
            j = len(nums2)-1
            for i in range(len(nums1)-1,0,-1):
                if nums1[i] is 0:
                    nums1[i] = nums2[j]
                    j = j - 1
                    if j < 0:
                        break
            nums1.sort()

#------------------------------------------------------------------------------------
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length.


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0 
        while i < len(nums):
            if(nums[i] == val):
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)

# #-------------------------------------------------------------------------------------
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums)-1:
            if(nums[i] == nums[i+1]):
                nums.pop(i)
            else:
                i += 1
        return len(nums)
#------------------------------------------------------------------------------------------
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.




class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        square_array = [x*2 for x in arr]
        if (arr.count(0) > 1) or (arr.count(1) > 1):
            return True
        elif len(arr) <= 1:
            return False
        else:
            for value in square_array:
                if (value in arr) and (value is not 0):
                    return True
        return False
#--------------------------------------------------------------------------------------------
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        flag = 0
        while flag < len(nums):
            if nums[i] is 0:
                nums.pop(i)
                nums.append(0)
            else: 
                i = i + 1
            flag += 1

#----------------------------------------------------------------------------------------------
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = arr[-1]
        i = len(arr)-1
        while i >= 0:
            temp = arr[i]
            arr[i] = max_value
            max_value = max(temp,max_value)
            i = i - 1
            
        
        arr[-1] = -1
        return arr