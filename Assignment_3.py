#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return target

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum

# Example usage
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)


# ## Question 2

# In[3]:


def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    quadruplets = []

    for i in range(n - 3):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates for the third element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1

                    # Skip duplicates for the fourth element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)


# ## Question 3

# In[5]:


def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first decreasing element from right to left
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        j = n - 1
        # Find the smallest element greater than nums[i]
        while j > i and nums[j] <= nums[i]:
            j -= 1
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the suffix from index i+1
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)


# ## Question 4

# In[6]:


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage
nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(result)


# ## Question 5

# In[7]:


def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        if digits[i] <= 9:
            carry = 0
            break
        digits[i] = 0

    if carry == 1:
        digits.insert(0, 1)

    return digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)


# ## QUestion 6

# In[8]:


def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)


# ## Question 7

# In[9]:


def findMissingRanges(nums, lower, upper):
    missingRanges = []
    start = lower

    for num in nums:
        if num > start:
            missingRanges.append(formatRange(start, num - 1))
        start = num + 1

    if start <= upper:
        missingRanges.append(formatRange(start, upper))

    return missingRanges

def formatRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

# Example usage
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)


# ## Question 8

# In[10]:


def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)


# In[ ]:




