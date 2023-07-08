#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


def isPowerOfTwo(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0


print(isPowerOfTwo(1))  
print(isPowerOfTwo(16))  
print(isPowerOfTwo(3))  


# ## Question 2

# In[3]:


def sumOfNaturalNumbers(n):
    return (n * (n + 1)) // 2


print(sumOfNaturalNumbers(3))  # Output: 6
print(sumOfNaturalNumbers(5))  # Output: 15


# ## Question 3

# In[9]:


def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result


print(factorial(25))  # Output: 120


# ## Question 4

# In[11]:


def power(N, P):
    return N ** P

print(power(5, 2))  # Output: 25
print(power(2, 5))  # Output: 32


# ## Question 5

# In[12]:


def findMax(arr, n):
    # Base case: if there is only one element in the array
    if n == 1:
        return arr[0]

    # Recursive case: find the maximum element in the remaining array
    max_element = findMax(arr, n - 1)

    # Compare the maximum element with the current element
    if arr[n - 1] > max_element:
        return arr[n - 1]
    else:
        return max_element

# Example usage
arr = [1, 4, 3, -5, -4, 8, 6]
print(findMax(arr, len(arr)))  # Output: 8

arr = [1, 4, 45, 6, 10, -8]
print(findMax(arr, len(arr)))  # Output: 45


# ## Question 6

# In[14]:


def findNthTerm(a, d, N):
    nth_term = a + (N - 1) * d
    return nth_term

# Example usage
a = 2
d = 1
N = 5
print(findNthTerm(a, d, N))  # Output: 6

a = 5
d = 2
N = 10
print(findNthTerm(a, d, N))  # Output: 23


# ## Question 7

# In[16]:


def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]  # backtrack

def printPermutations(string):
    n = len(string)
    s = list(string)
    permute(s, 0, n - 1)

# Example usage
string = "ABC"
printPermutations(string)

string = "XY"
printPermutations(string)


# ## Question 8

# In[17]:


def getProduct(arr):
    product = 1
    for num in arr:
        product *= num
    return product

# Example usage
arr = [1, 2, 3, 4, 5]
result = getProduct(arr)
print(result)

arr = [1, 6, 3]
result = getProduct(arr)
print(result)


# In[ ]:




