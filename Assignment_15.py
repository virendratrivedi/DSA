#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


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


# ## Quesion 2

# In[2]:


def findNextGreaterElements(arr):
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result

# Test Scenario
arr = [1, 3, 2, 4]

# Testing the function
print(findNextGreaterElements(arr))  # Output: [3, 4, 4, -1]


# ## Question 3

# In[3]:


class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def push(self, value):
        self.q1.append(value)
    
    def pop(self):
        if not self.q1:
            return -1
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        
        pop_value = self.q1.pop(0)
        
        self.q1, self.q2 = self.q2, self.q1
        
        return pop_value

# Test Scenarios
stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
stack.push(4)
print(stack.pop())  # Output: 4


# ## Question 4

# In[4]:


def reverse_stack(stack):
    if len(stack) > 0:
        # Remove the top element from the stack
        top = stack.pop()

        # Reverse the remaining stack
        reverse_stack(stack)

        # Insert the top element at the bottom of the reversed stack
        insert_at_bottom(stack, top)

def insert_at_bottom(stack, value):
    if len(stack) == 0:
        stack.append(value)
    else:
        # Remove the top element from the stack
        top = stack.pop()

        # Insert the value at the bottom of the stack
        insert_at_bottom(stack, value)

        # Insert the removed top element back onto the stack
        stack.append(top)

# Test Scenarios
stack = [3, 2, 1, 7, 6]
reverse_stack(stack)
print(stack)  # Output: [6, 7, 1, 2, 3]

stack = [4, 3, 9, 6]
reverse_stack(stack)
print(stack)  # Output: [6, 9, 3, 4]


# ## Question 5

# In[5]:


def reverse_string(string):
    stack = []
    reversed_string = ""

    # Push each character of the string onto the stack
    for char in string:
        stack.append(char)

    # Pop each character from the stack and append it to the reversed string
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Test Scenario
S = "GeeksforGeeks"
reversed_S = reverse_string(S)
print(reversed_S)  # Output: skeeGrofskeeG


# ## Question 6

# In[6]:


def evaluate_postfix(expression):
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        if char.isdigit():
            # If the character is a digit, push it onto the stack
            stack.append(int(char))
        else:
            # If the character is an operator, pop two operands from the stack and perform the operation
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            # Push the result back onto the stack
            stack.append(result)

    # The final result is the only element remaining on the stack
    return stack[0]

# Test Scenario
S = "231*+9-"
result = evaluate_postfix(S)
print(result)  # Output: -4


# ## Question 7

# In[7]:


class MinStack:
    def __init__(self):
        self.stack = []  # Stack to store the elements
        self.min_stack = []  # Stack to store the minimum values

    def push(self, val):
        self.stack.append(val)

        # If the min_stack is empty or the new value is smaller than or equal to the current minimum,
        # push the new value onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        # If the value being popped is the current minimum, also pop it from the min_stack
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Test Scenario
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2


# ## Question 8

# In[8]:


def trap(height):
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1  # Pointers to the leftmost and rightmost bars
    left_max, right_max = 0, 0  # Variables to track the maximum heights encountered

    water = 0  # Variable to store the total trapped water

    while left < right:
        # Update the left_max and right_max if necessary
        if height[left] > left_max:
            left_max = height[left]
        if height[right] > right_max:
            right_max = height[right]

        # Calculate the amount of water that can be trapped at the current position
        if left_max < right_max:
            water += left_max - height[left]
            left += 1
        else:
            water += right_max - height[right]
            right -= 1

    return water

# Test Scenario
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6


# In[ ]:




