#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


def romanToInt(s):
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for c in s:
        current_value = roman_to_int[c]
        
        if current_value > prev_value:
            total -= prev_value
        else:
            total += prev_value
        
        prev_value = current_value
    
    total += prev_value
    
    return total


# ## Question 2

# In[4]:


def lengthOfLongestSubstring(s):
    n = len(s)
    seen = set()
    max_length = 0
    start = 0
    end = 0
    
    while end < n:
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            seen.remove(s[start])
            start += 1
    
    return max_length

s6 = "abcdefghijklmnopqrstuvwxyz"
# The longest substring without repeating characters is the entire string with a length of 26

# Test Case 7: String with multiple longest substrings
s7 = "abcdeabcde"
# The longest substring without repeating characters is "abcde" with a length of 5

# Testing the function
print(lengthOfLongestSubstring(s6))  # Output: 3
print(lengthOfLongestSubstring(s7))


# ## Question 3 

# In[5]:


from typing import List

def majorityElement(nums: List[int]) -> int:
    counts = {}  # Dictionary to store the counts of each element
    
    # Count the occurrences of each element
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Find the majority element
    for num, count in counts.items():
        if count > len(nums) // 2:
            return num

# Test Scenario
nums = [3, 2, 3]
# The majority element is 3 since it appears twice, which is more than len(nums) // 2

# Testing the function
print(majorityElement(nums))  # Output: 3


# ## Question 4

# In[6]:


from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = {}  # Dictionary to store the groups of anagrams
    
    # Group the anagrams
    for word in strs:
        sorted_word = "".join(sorted(word))  # Sort the letters of the word
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]
    
    return list(groups.values())

# Test Scenario
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# The anagrams are ["eat", "tea", "ate"], ["tan", "nat"], and ["bat"]

# Testing the function
print(groupAnagrams(strs))  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


# ## Question 5

# In[7]:


def nthUglyNumber(n: int) -> int:
    ugly_nums = [1]  # List to store the ugly numbers
    p2, p3, p5 = 0, 0, 0  # Pointers for multiplying factors 2, 3, and 5
    
    # Generate the ugly numbers
    while len(ugly_nums) < n:
        next_ugly = min(ugly_nums[p2] * 2, ugly_nums[p3] * 3, ugly_nums[p5] * 5)
        ugly_nums.append(next_ugly)
        
        if next_ugly == ugly_nums[p2] * 2:
            p2 += 1
        if next_ugly == ugly_nums[p3] * 3:
            p3 += 1
        if next_ugly == ugly_nums[p5] * 5:
            p5 += 1
    
    return ugly_nums[-1]

# Test Scenario
n = 10

# Testing the function
print(nthUglyNumber(n))  # Output: 12


# ## Question 6

# In[9]:


from collections import Counter

def topKFrequent(words, k):
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Sort the words based on frequency and lexicographical order
    sorted_words = sorted(word_counts.keys(), key=lambda x: (-word_counts[x], x))
    
    # Return the top k frequent words
    return sorted_words[:k]

# Test Scenario
words = ["i", "love", "Zombie", "i", "love", "coding"]
k = 2

# Testing the function
print(topKFrequent(words, k))  # Output: ["i", "love"]


# ## Question 7

# In[10]:


from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    window = deque()
    
    for i, num in enumerate(nums):
        # Remove elements outside the current window from the front of the deque
        while window and window[0] <= i - k:
            window.popleft()
        
        # Remove elements smaller than the current element from the rear of the deque
        while window and nums[window[-1]] < num:
            window.pop()
        
        # Add the current element index to the rear of the deque
        window.append(i)
        
        # Add the maximum element in the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

# Test Scenario
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# Testing the function
print(maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]


# ## Question 8

# In[11]:


def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]

# Test Scenario
arr = [1, 2, 3, 4, 5]
k = 4
x = 3

# Testing the function
print(findClosestElements(arr, k, x))  # Output: [1, 2, 3, 4]


# In[ ]:




