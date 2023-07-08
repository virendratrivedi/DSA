#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[3]:


def findPermutation(s):
    n = len(s)
    perm = [0] * (n + 1)
    
    # Initialize the permutation in ascending order
    for i in range(n + 1):
        perm[i] = i + 1
    
    # Reconstruct the permutation based on the string
    i = 0
    while i < n:
        j = i
        while i < n and s[i] == 'D':
            i += 1
        reverse(perm, j, i+1)  # Reverse the subarray for 'D' sequence
        i += 1
    
    return perm

# Helper function to reverse a subarray in-place
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end-1] = arr[end-1], arr[start]
        start += 1
        end -= 1

# Example usage
s = "IDID"
perm = findPermutation(s)
print(perm)


# ## Question 2

# In[4]:


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example usage
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = searchMatrix(matrix, target)
print(result)


# ## Question 3 

# In[6]:


def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    # Check for increasing sequence
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    # Check for decreasing sequence
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

# Example usage
arr = [2, 1]
result = validMountainArray(arr)
print(result)


# ## Question 4

# In[5]:


def findMaxLength(nums):
    counter = {0: -1}
    max_length = 0
    curr_count = 0

    for i in range(len(nums)):
        curr_count += 1 if nums[i] == 1 else -1

        if curr_count in counter:
            max_length = max(max_length, i - counter[curr_count])
        else:
            counter[curr_count] = i

    return max_length

# Example usage
nums = [0, 1]
result = findMaxLength(nums)
print(result)


# ## Question 5

# In[7]:


def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)

    product_sum = 0
    for i in range(len(nums1)):
        product_sum += nums1[i] * nums2[i]

    return product_sum


# Example usage
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
result = minProductSum(nums1, nums2)
print(result)  # Output: 40


# ## Question 6

# In[9]:


def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # Invalid length, return empty array

    count = {}
    for num in changed:
        count[num] = count.get(num, 0) + 1

    changed.sort()  # Sort the changed array

    original = []
    for num in changed:
        if count[num] == 0:
            continue
        if count[num] > 0 and count.get(num * 2, 0) > 0:
            count[num] -= 1
            count[num * 2] -= 1
            original.append(num)
        else:
            return []  # Doubling condition violated

    return original


# Example usage
changed = [1, 3, 4, 2, 6, 8]
original = findOriginalArray(changed)
print(original)  # Output: [1, 3, 4]


# ## Question 7

# In[10]:


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]  # Initialize the matrix with zeros
    num = 1  # Starting number

    # Initialize boundaries
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while num <= n * n:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


# Example usage
n = 3
matrix = generateMatrix(n)
for row in matrix:
    print(row)
# Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


# ## Question 8

# In[11]:


def multiply(mat1, mat2):
    m = len(mat1)  # Number of rows in mat1
    k = len(mat1[0])  # Number of columns in mat1
    n = len(mat2[0])  # Number of columns in mat2

    # Initialize the result matrix with zeros
    result = [[0] * n for _ in range(m)]

    # Perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for l in range(k):
                result[i][j] += mat1[i][l] * mat2[l][j]

    return result


# Example usage
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
result = multiply(mat1, mat2)
for row in result:
    print(row)
# Output: [[7, 0, 0], [-7, 0, 3]]


# In[ ]:




