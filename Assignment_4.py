#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


def arraysIntersection(arr1, arr2, arr3):
    result = []
    p1, p2, p3 = 0, 0, 0
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr2[p2] < arr3[p3]:
            p2 += 1
        else:
            p3 += 1
    return result

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = arraysIntersection(arr1, arr2, arr3)
print(result)


# ## Question 2

# In[2]:


def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer = []
    answer.append(list(set1 - set2))
    answer.append(list(set2 - set1))

    return answer

# Example usage
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)


# ## Question 4

# In[3]:


def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    total_sum = 0
    for i in range(0, len(nums), 2):
        total_sum += nums[i]
    return total_sum

# Example usage
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)


# ## Question 6

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


# ## Question 8

# In[5]:


def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

# Example usage
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)


# In[ ]:




