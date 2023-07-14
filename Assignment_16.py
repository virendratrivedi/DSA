#!/usr/bin/env python
# coding: utf-8

# ## Answer 1

# In[1]:


from collections import defaultdict

def find_next_greater_frequency(array):
    frequency_dict = defaultdict(int)
    next_greater_dict = {}

    result = []

    for i in range(len(array) - 1, -1, -1):
        frequency_dict[array[i]] += 1

    for i in range(len(array) - 1, -1, -1):
        frequency = frequency_dict[array[i]]
        next_greater_dict[array[i]] = -1

        for j in range(i + 1, len(array)):
            if frequency_dict[array[j]] > frequency:
                next_greater_dict[array[i]] = array[j]
                break

    for num in array:
        result.append(next_greater_dict[num])

    return result

# Example usage:
arr = [1, 1, 2, 3, 4, 2, 1]
result = find_next_greater_frequency(arr)
print(result)  # Output: [-1, -1, 1, 2, 2, 1, -1]


# ## Answer 2

# In[2]:


def sort_stack(stack):
    temp_stack = []

    while stack:
        current_element = stack.pop()

        while temp_stack and temp_stack[-1] > current_element:
            stack.append(temp_stack.pop())

        temp_stack.append(current_element)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack

# Example usage:
stack = [34, 3, 31, 98, 92, 23]
result = sort_stack(stack)
print(result)  # Output: [3, 23, 31, 34, 92, 98]


# ## Answer 3

# In[3]:


def delete_middle(stack, index):
    if index == 0:
        stack.pop()
        return

    temp = stack.pop()
    delete_middle(stack, index - 1)
    stack.append(temp)

def delete_middle_element(stack):
    size = len(stack)
    middle_index = size // 2

    delete_middle(stack, middle_index)

    return stack

# Example usage:
stack = [1, 2, 3, 4, 5]
result = delete_middle_element(stack)
print(result)  # Output: [1, 2, 4, 5]

stack = [1, 2, 3, 4, 5, 6]
result = delete_middle_element(stack)
print(result)  # Output: [1, 2, 4, 5, 6]


# ## Answer 4

# In[6]:


from queue import Queue

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def arrange_in_increasing_order(queue):
    stack = Stack()
    second_queue = Queue()
    expected_element = 1

    while not queue.empty():
        if queue.get() == expected_element:
            second_queue.put(expected_element)
            expected_element += 1
        else:
            if stack.is_empty() or stack.top() > queue.queue[0]:
                stack.push(queue.get())
            else:
                return "No"

    while not stack.is_empty():
        if stack.top() == expected_element:
            second_queue.put(stack.pop())
            expected_element += 1
        else:
            return "No"

    if not stack.is_empty():
        return "No"

    return "Yes"

# Example usage:
queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)

result = arrange_in_increasing_order(queue)
print(result)  # Output: Yes

queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(6)
queue.put(3)
queue.put(4)

result = arrange_in_increasing_order(queue)
print(result)  # Output: No


# ## Answer 5

# In[7]:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def reverse_number(number):
    number_str = str(number)
    stack = Stack()

    for char in number_str:
        stack.push(char)

    reversed_str = ""

    while not stack.is_empty():
        reversed_str += stack.pop()

    reversed_number = int(reversed_str)

    return reversed_number

# Example usage:
number = 365
reversed_number = reverse_number(number)
print(reversed_number)  # Output: 563

number = 6899
reversed_number = reverse_number(number)
print(reversed_number)  # Output: 9986


# ## Answer 6

# In[1]:


from queue import Queue

def reverse_k_elements(queue, k):
    new_queue = Queue()
    count = 0

    # Dequeue and enqueue the front elements of the original queue into the new queue
    while count < k:
        front_element = queue.get()
        new_queue.put(front_element)
        count += 1

    # Dequeue remaining elements from the original queue and enqueue them back
    while not queue.empty():
        new_queue.put(queue.get())

    # Dequeue elements from the new queue and enqueue them back into the original queue
    while not new_queue.empty():
        queue.put(new_queue.get())

    return queue

# Example usage:
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

k = 3

reversed_queue = reverse_k_elements(queue, k)

# Printing the modified queue
while not reversed_queue.empty():
    print(reversed_queue.get(), end=" ")  # Output: 3 2 1 4 5


# ## Answer 7

# In[2]:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def count_words_after_destruction(sequence):
    stack = Stack()

    for word in sequence:
        if stack.is_empty() or word != stack.top():
            stack.push(word)
        else:
            stack.pop()

    return len(stack.stack)

# Example usage:
sequence = ['ab', 'aa', 'aa', 'bcd', 'ab']
result = count_words_after_destruction(sequence)
print(result)  # Output: 3

sequence = ['tom', 'jerry', 'jerry', 'tom']
result = count_words_after_destruction(sequence)
print(result)  # Output: 0


# ## Answer 8

# In[3]:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def max_absolute_difference(arr):
    n = len(arr)
    left_smaller = [0] * n
    right_smaller = [0] * n
    stack = Stack()

    # Compute the nearest smaller element on the left side
    for i in range(n):
        while not stack.is_empty() and stack.top() >= arr[i]:
            stack.pop()

        if not stack.is_empty():
            left_smaller[i] = stack.top()

        stack.push(arr[i])

    stack.stack.clear()

    # Compute the nearest smaller element on the right side
    for i in range(n - 1, -1, -1):
        while not stack.is_empty() and stack.top() >= arr[i]:
            stack.pop()

        if not stack.is_empty():
            right_smaller[i] = stack.top()

        stack.push(arr[i])

    max_diff = 0

    # Compute the maximum absolute difference
    for i in range(n):
        diff = abs(left_smaller[i] - right_smaller[i])
        max_diff = max(max_diff, diff)

    return max_diff

# Example usage:
arr = [2, 1, 8]
result = max_absolute_difference(arr)
print(result)  # Output: 1

arr = [2, 4, 8, 7, 7, 9, 3]
result = max_absolute_difference(arr)
print(result)  # Output: 4

arr = [5, 1, 9, 2, 5, 1, 7]
result = max_absolute_difference(arr)
print(result)  # Output: 1


# In[ ]:




