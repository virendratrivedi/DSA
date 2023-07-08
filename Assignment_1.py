#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[2]:


def twoSum(nums, target):
    complement_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)


# ## Question 2

# In[3]:


def removeElement(nums, val):
    k = 0  # Number of elements not equal to val
    
    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k

# Example usage
nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print("k =", result)
print("nums =", nums[:result] + ["_*"] * (len(nums) - result))


# ## Question 3

# In[5]:


def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(result)


# ## Question 4

# In[6]:


def plusOne(digits):
    num = int(''.join(map(str, digits)))  # Convert the array of digits to an integer
    num += 1  # Increment the integer by one
    return list(map(int, str(num)))  # Convert the incremented integer back to an array of digits

digits = [1, 2, 3]
result = plusOne(digits)
print(result)


# ## Question 5

# In[7]:


def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    # Merge the arrays from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # Copy any remaining elements from nums2 to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)


# ## Question 6

# In[8]:


def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Example usage
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)


# ## QUestion 7

# In[9]:


def moveZeroes(nums):
    zero_count = nums.count(0)
    nums[:] = [num for num in nums if num != 0]
    nums += [0] * zero_count

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)


# ## Question 8

# In[10]:


def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    total_sum = (n * (n + 1)) // 2

    # Iterate through the array
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)
        total_sum -= num

    missing = total_sum + duplicate

    return [duplicate, missing]

# Example usage
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)


# In[ ]:




