#!/usr/bin/env python
# coding: utf-8

# ## Answer 1

# In[1]:


def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Example usage
n = 1
result = isPowerOfTwo(n)
print(result)

n = 16
result = isPowerOfTwo(n)
print(result)

n = 3
result = isPowerOfTwo(n)
print(result)


# ## Answer 2

# In[2]:


def sumOfFirstN(n):
    return (n * (n + 1)) // 2

# Example usage
n = 3
result = sumOfFirstN(n)
print(result)

n = 5
result = sumOfFirstN(n)
print(result)


# ## Answer 3

# In[3]:


def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

# Example usage
N = 5
result = factorial(N)
print(result)

N = 4
result = factorial(N)
print(result)


# ## Answer 4

# In[4]:


def exponent(N, P):
    return N ** P

# Example usage
N = 5
P = 2
result = exponent(N, P)
print(result)

N = 2
P = 5
result = exponent(N, P)
print(result)


# ## Answer 5

# In[5]:


def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], findMax(arr[1:]))

# Example usage
arr = [1, 4, 3, -5, -4, 8, 6]
result = findMax(arr)
print(result)

arr = [1, 4, 45, 6, 10, -8]
result = findMax(arr)
print(result)


# ## Answer 6

# In[6]:


def nthTermAP(a, d, N):
    return a + (N - 1) * d

# Example usage
a = 2
d = 1
N = 5
result = nthTermAP(a, d, N)
print(result)

a = 5
d = 2
N = 10
result = nthTermAP(a, d, N)
print(result)


# ## Answer 7

# In[7]:


def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # Swap characters
            permute(s, l + 1, r)  # Recursive call
            s[l], s[i] = s[i], s[l]  # Revert the swap

# Example usage
S = "ABC"
n = len(S)
permute(list(S), 0, n - 1)

S = "XY"
n = len(S)
permute(list(S), 0, n - 1)


# ## Answer 8

# In[9]:


def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product

# Example usage
arr = [1, 2, 3, 4, 5]
result = productOfArray(arr)
print(result)

arr = [1, 6, 3]
result = productOfArray(arr)
print(result)


# In[ ]:




