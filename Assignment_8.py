#!/usr/bin/env python
# coding: utf-8

# ## Answer 1:- 

# In[1]:


def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

    return dp[m][n]

# Example usage
s1 = "sea"
s2 = "eat"
result = minimumDeleteSum(s1, s2)
print(result)


# ## Answer 2:- 

# In[2]:


def isValid(s):
    stack = []
    star_stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == '*':
            star_stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    while stack and star_stack:
        if stack[-1] > star_stack[-1]:
            return False
        stack.pop()
        star_stack.pop()

    return len(stack) == 0

# Example usage
s = "()"
result = isValid(s)
print(result)


# ## Answer 3:- 

# In[3]:


def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i

    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Example usage
word1 = "sea"
word2 = "eat"
result = minDistance(word1, word2)
print(result)


# ## Answer 4:- 

# In[4]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    def build_tree(s, i):
        if i >= len(s) or s[i] == ')':
            return None

        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()):
            i += 1

        val = int(s[start:i])
        node = TreeNode(val)

        if i < len(s) and s[i] == '(':
            node.left, i = build_tree(s, i + 1)

        if i < len(s) and s[i] == '(':
            node.right, i = build_tree(s, i + 1)

        return node, i + 1

    if not s:
        return None

    root, _ = build_tree(s, 0)
    return root

def inorder_traversal(root):
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result

# Example usage
s = "4(2(3)(1))(6(5))"
root = str2tree(s)
result = inorder_traversal(root)
print(result)


# ## Answer 5

# In[6]:


def compress(chars):
    # Helper function to convert an integer to a list of characters
    def int_to_chars(n):
        if n == 1:
            return []
        return list(str(n))

    n = len(chars)
    write = 0  # Position to write the compressed characters
    count = 1  # Counter for consecutive repeating characters

    for read in range(1, n):
        if chars[read] == chars[read-1]:
            count += 1
        else:
            chars[write] = chars[read-1]
            write += 1

            for c in int_to_chars(count):
                chars[write] = c
                write += 1

            count = 1

    # Write the last set of characters
    chars[write] = chars[n-1]
    write += 1

    for c in int_to_chars(count):
        chars[write] = c
        write += 1

    return write

# Example usage
chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print("New length:", new_length)
print("Compressed array:", chars[:new_length])


# ## Answer 6

# In[7]:


from collections import Counter

def findAnagrams(s, p):
    result = []
    p_freq = Counter(p)
    window_freq = Counter(s[:len(p)])  # Initialize the frequency map for the first window

    # Compare the frequency maps for the first window
    if window_freq == p_freq:
        result.append(0)

    # Slide the window and update the frequency map
    for i in range(len(p), len(s)):
        # Remove the leftmost character from the window
        if window_freq[s[i - len(p)]] == 1:
            del window_freq[s[i - len(p)]]
        else:
            window_freq[s[i - len(p)]] -= 1

        # Add the rightmost character to the window
        window_freq[s[i]] += 1

        # Compare the frequency maps
        if window_freq == p_freq:
            result.append(i - len(p) + 1)

    return result

# Example usage
s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)


# ## Answer 7:- 

# In[8]:


def decodeString(s):
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char.isalpha():
            current_string += char
        elif char == "[":
            stack.append(current_string)
            stack.append(current_num)
            current_string = ""
            current_num = 0
        elif char == "]":
            num = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + num * current_string

    return current_string

# Example usage
s = "3[a]2[bc]"
result = decodeString(s)
print(result)


# ## Answer 8

# In[9]:


def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if there are any repeated characters in s
        return len(set(s)) < len(s)

    # Find the indices of mismatched characters
    indices = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            indices.append(i)

    # Check if there are exactly two mismatched characters
    if len(indices) != 2:
        return False

    # Check if swapping the characters produces goal
    return s[indices[0]] == goal[indices[1]] and s[indices[1]] == goal[indices[0]]

# Example usage
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)


# In[ ]:




