#!/usr/bin/env python
# coding: utf-8

# ## Answer 1:- 

# In[1]:


import math

def isPowerOfThree(n):
    if n <= 0:
        return False

    x = math.log(n, 3)
    return abs(x - round(x)) < 1e-10

# Example usage
n = 27
result = isPowerOfThree(n)
print(result)


# ## Answer 2

# In[3]:


def lastRemaining(n):
    start = 1
    step = 2
    left_to_right = True

    while n > 1:
        if left_to_right or n % 2 == 1:
            start += step

        n //= 2
        step *= 2
        left_to_right = not left_to_right

    return start

# Example usage
n = 9
result = lastRemaining(n)
print(result)

n = 1
result = lastRemaining(n)
print(result)


# ## Answer 3

# In[4]:


def printSubsets(s, curr="", index=0):
    if index == len(s):
        print(curr)
        return

    # Exclude current character
    printSubsets(s, curr, index + 1)

    # Include current character
    printSubsets(s, curr + s[index], index + 1)

# Example usage
s = "abc"
printSubsets(s)

s = "abcd"
printSubsets(s)


# ## Answer 4

# In[5]:


def stringLength(s):
    if s == "":
        return 0
    else:
        return 1 + stringLength(s[1:])

# Example usage
str1 = "abcd"
result1 = stringLength(str1)
print(result1)

str2 = "GEEKSFORGEEKS"
result2 = stringLength(str2)
print(result2)


# ## Answer 5

# In[6]:


def countSubstrings(s):
    count = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1

    return count

# Example usage
S = "abcab"
result = countSubstrings(S)
print(result)

S = "aba"
result = countSubstrings(S)
print(result)


# ## Answer 7

# In[7]:


def permute(s, left, right):
    if left == right:
        print("".join(s))
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]  # Swap characters
            permute(s, left + 1, right)
            s[left], s[i] = s[i], s[left]  # Backtrack (undo the swap)

def printPermutations(str):
    n = len(str)
    s = list(str)
    permute(s, 0, n - 1)

# Example usage
str1 = "cd"
printPermutations(str1)

str2 = "abb"
printPermutations(str2)


# ## Answer 8

# In[8]:


def countConsonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    for char in s:
        if char in consonants:
            count += 1

    return count

# Example usage
str1 = "abc de"
result1 = countConsonants(str1)
print(result1)

str2 = "geeksforgeeks portal"
result2 = countConsonants(str2)
print(result2)


# In[ ]:




