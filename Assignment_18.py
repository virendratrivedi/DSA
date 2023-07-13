#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times
    merged = [intervals[0]]  # Initialize the merged list with the first interval

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            # Overlapping intervals, merge them by updating the end time of the last interval
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # Non-overlapping interval, append it to the merged list
            merged.append(interval)

    return merged

# Test Scenario
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]


# ## Question 2

# In[2]:


def sortColors(nums):
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Test Scenario
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


# ## Question 3

# In[3]:


def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


# ## Question 4

# In[5]:


def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    nums.sort()
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i-1])
    
    return max_gap


# Test scenario
nums = [7, 2, 9, 5, 1, 8]
expected_output = 4

# Test the maximumGap function
output = maximumGap(nums)
print("Output:", output)
print("Expected Output:", expected_output)
print("Test Result:", "Passed" if output == expected_output else "Failed")


# ## Question 5

# In[6]:


def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False


# Test scenario
nums = [1, 2, 3, 1]
expected_output = True

# Test the containsDuplicate function
output = containsDuplicate(nums)
print("Output:", output)
print("Expected Output:", expected_output)
print("Test Result:", "Passed" if output == expected_output else "Failed")


# ## Question 6

# In[7]:


def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]

    for start, point_end in points:
        if start > end:
            arrows += 1
            end = point_end

    return arrows


# Test scenario
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
expected_output = 2

# Test the findMinArrowShots function
output = findMinArrowShots(points)
print("Output:", output)
print("Expected Output:", expected_output)
print("Test Result:", "Passed" if output == expected_output else "Failed")


# ## Question 7

# In[8]:


def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1's

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test scenario
nums = [10, 9, 2, 5, 3, 7, 101, 18]
expected_output = 4

# Test the lengthOfLIS function
output = lengthOfLIS(nums)
print("Output:", output)
print("Expected Output:", expected_output)
print("Test Result:", "Passed" if output == expected_output else "Failed")


# ## Question 8

# In[9]:


def find132pattern(nums):
    stack = []
    s3 = float('-inf')

    for num in reversed(nums):
        if num < s3:
            return True
        while stack and num > stack[-1]:
            s3 = max(s3, stack.pop())
        stack.append(num)

    return False


# Test scenario
nums = [1, 2, 3, 4]
expected_output = False

# Test the find132pattern function
output = find132pattern(nums)
print("Output:", output)
print("Expected Output:", expected_output)
print("Test Result:", "Passed" if output == expected_output else "Failed")


# In[ ]:




