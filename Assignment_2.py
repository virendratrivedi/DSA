#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum


nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)


# ## Question 2

# In[3]:


def distributeCandies(candyType):
    max_candies = len(candyType) // 2
    unique_candies = len(set(candyType))
    return min(unique_candies, max_candies)

# Example usage
candyType = [1, 1, 2, 2, 3, 3]
result = distributeCandies(candyType)
print(result)


# ## Question 3

# In[4]:


def findLHS(nums):
    num_freq = {}
    max_length = 0

    # Count the frequency of each number
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    # Calculate the length of the longest harmonious subsequence
    for num in num_freq:
        if num + 1 in num_freq:
            length = num_freq[num] + num_freq[num + 1]
            max_length = max(max_length, length)

    return max_length

# Example usage
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)


# ## Question 4

# In[7]:


def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0

    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
            i += 1

        if count >= n:
            return True
        
        i += 1
    
    return False


flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
print(result)


# ## Question 5

# In[6]:


def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    return max(nums[n-1] * nums[n-2] * nums[n-3], nums[0] * nums[1] * nums[n-1])

# Example usage
nums = [1, 2, 3]
result = maximumProduct(nums)
print(result)


# ## Question 6

# In[8]:


def search(nums, target):
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

    return -1

# Example usage
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
print(result)


# ## Question 7

# In[9]:


def isMonotonic(nums):
    n = len(nums)
    increasing = decreasing = True

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            increasing = False
        if nums[i] < nums[i + 1]:
            decreasing = False

    return increasing or decreasing

# Example usage
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
print(result)


# ## Question 8

# In[10]:


def minimumScore(nums, k):
    min_num = min(nums)
    max_num = max(nums)
    
    if min_num + k >= max_num - k:
        return 0
    
    return max_num - min_num - 2 * k

# Example usage
nums = [1]
k = 0
result = minimumScore(nums, k)
print(result)


# In[ ]:




