#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[2]:


def construct2DArray(original, m, n):
    if m * n != len(original):
        return []
    
    result = [[0] * n for _ in range(m)]
    for i in range(len(original)):
        row = i // n
        col = i % n
        result[row][col] = original[i]
    
    return result

# Example usage
original = [1, 2, 3, 4]
m = 2
n = 2
result = construct2DArray(original, m, n)
print(result)


# ## Question 2

# In[3]:


def arrangeCoins(n):
    k = 0
    while n >= k:
        k += 1
        n -= k
    return k - 1

# Example usage
n = 5
result = arrangeCoins(n)
print(result)


# ## Question 3

# In[4]:


def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    i = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1
        i -= 1

    return result

# Example usage
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)


# ## Question 4

# In[5]:


def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result = [list(set1 - set2), list(set2 - set1)]
    return result

# Example usage
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)


# ## Question 5

# In[6]:


def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for num1 in arr1:
        has_close_element = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                has_close_element = True
                break
        if not has_close_element:
            count += 1
    return count

# Example usage
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
result = findTheDistanceValue(arr1, arr2, d)
print(result)


# ## Question 6

# In[7]:


def findDuplicates(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    return result

# Example usage
nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = findDuplicates(nums)
print(result)


# ## Question 7

# In[8]:


def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the mid element is greater than the rightmost element
        if nums[mid] > nums[right]:
            left = mid + 1
        # Check if the mid element is less than the rightmost element
        elif nums[mid] < nums[right]:
            right = mid
        # If the mid element is equal to the rightmost element,
        # we can exclude the rightmost element and continue the search
        else:
            right -= 1

    return nums[left]

# Example usage
nums = [3, 4, 5, 1, 2]
result = findMin(nums)
print(result)


# ## Question 8

# In[11]:


from collections import Counter

def findOriginalArray(changed):
    n = len(changed)
    if n % 2 != 0:
        return []  # If the length of 'changed' is odd, it cannot be a doubled array

    original = []
    counter = Counter(changed)  # Count the frequency of each element in 'changed'

    for num in sorted(changed):
        if counter[num] > 0 and counter[num * 2] > 0:
            original.append(num)
            counter[num] -= 1
            counter[num * 2] -= 1

    if sum(counter.values()) == 0:
        return original
    else:
        return []

# Example usage
changed = [1, 3, 4, 2, 6, 8]
original = findOriginalArray(changed)
print(original)


# In[ ]:




