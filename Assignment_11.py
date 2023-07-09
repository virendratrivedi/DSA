#!/usr/bin/env python
# coding: utf-8

# ## Answer 1

# In[1]:


def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        sqrt = x // mid

        if sqrt == mid:
            return mid
        elif sqrt < mid:
            right = mid - 1
        else:
            left = mid + 1

    return right

# Example usage
x1 = 4
result1 = mySqrt(x1)
print(result1)

x2 = 8
result2 = mySqrt(x2)
print(result2)


# ## Answer 2

# In[2]:


def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage
nums1 = [1, 2, 3, 1]
result1 = findPeakElement(nums1)
print(result1)

nums2 = [1, 2, 1, 3, 5, 6, 4]
result2 = findPeakElement(nums2)
print(result2)


# ## Answer 3

# In[3]:


def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage
nums1 = [3, 0, 1]
result1 = missingNumber(nums1)
print(result1)

nums2 = [0, 1]
result2 = missingNumber(nums2)
print(result2)

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
result3 = missingNumber(nums3)
print(result3)


# ## Answer 4

# In[4]:


def findDuplicate(nums):
    slow = fast = nums[0]

    # Phase 1: Find the intersection point of the two pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the starting point of the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage
nums1 = [1, 3, 4, 2, 2]
result1 = findDuplicate(nums1)
print(result1)

nums2 = [3, 1, 3, 4, 2]
result2 = findDuplicate(nums2)
print(result2)


# ## Answer 5

# In[5]:


def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result1 = intersection(nums1, nums2)
print(result1)

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
result2 = intersection(nums3, nums4)
print(result2)


# ## Answer 6

# In[6]:


def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the middle element is greater than the last element
        if nums[mid] > nums[right]:
            left = mid + 1
        # Check if the middle element is less than the last element
        elif nums[mid] < nums[right]:
            right = mid
        # If the middle element is equal to the last element, decrement the right pointer
        else:
            right -= 1

    # At the end of the loop, left will be pointing to the minimum element
    return nums[left]

# Example usage
nums1 = [3, 4, 5, 1, 2]
result1 = findMin(nums1)
print(result1)

nums2 = [4, 5, 6, 7, 0, 1, 2]
result2 = findMin(nums2)
print(result2)

nums3 = [11, 13, 15, 17]
result3 = findMin(nums3)
print(result3)


# ## Answer 7

# In[7]:


def searchRange(nums, target):
    left = findLeftMost(nums, target)
    right = findRightMost(nums, target)

    return [left, right]

def findLeftMost(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def findRightMost(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = searchRange(nums, target)
print(result)

nums = [5, 7, 7, 8, 8, 10]
target = 6
result = searchRange(nums, target)
print(result)

nums = []
target = 0
result = searchRange(nums, target)
print(result)


# ## Answer 8

# In[8]:


from collections import Counter

def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    result = []
    for num in nums1:
        if num in counter2 and counter1[num] > 0 and counter2[num] > 0:
            result.append(num)
            counter1[num] -= 1
            counter2[num] -= 1

    return result

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersect(nums1, nums2)
print(result)


# In[ ]:




