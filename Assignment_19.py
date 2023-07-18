#!/usr/bin/env python
# coding: utf-8

# ## Answer:-1

# In[4]:


import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    # Create a min heap to store the first element of each linked list
    min_heap = []
    for head in lists:
        if head:
            heapq.heappush(min_heap, head)

    # Create a dummy node to start building the merged list
    dummy = ListNode()
    current = dummy

    while min_heap:
        # Get the smallest node from the min heap
        node = heapq.heappop(min_heap)

        # Append the smallest node to the merged list
        current.next = node
        current = current.next

        # Move to the next node in the linked list
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage
lists = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
result = mergeKLists(lists)

# Function to convert the result linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

print(linked_list_to_list(result)) # Output: [1, 1, 2, 3, 4, 4, 5, 6]


# ## Answer 2

# In[5]:


def countSmaller(nums):
    def merge_sort(arr, indices):
        if len(arr) <= 1:
            return arr, indices

        mid = len(arr) // 2
        left, left_indices = merge_sort(arr[:mid], indices[:mid])
        right, right_indices = merge_sort(arr[mid:], indices[mid:])
        merged, merged_indices = [], []
        i, j, count = 0, 0, 0

        while i < len(left) or j < len(right):
            if j == len(right) or (i < len(left) and left[i] <= right[j]):
                merged.append(left[i])
                merged_indices.append(left_indices[i])
                counts[left_indices[i]] += count
                i += 1
            else:
                merged.append(right[j])
                merged_indices.append(right_indices[j])
                count += 1
                j += 1

        return merged, merged_indices

    n = len(nums)
    counts = [0] * n
    indices = list(range(n))

    merge_sort(nums, indices)

    return counts

# Example usage
nums = [5, 2, 6, 1]
print(countSmaller(nums))  # Output: [2, 1, 1, 0]


# ## Answer 3

# In[6]:


def sortArray(nums):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    return merge_sort(nums)

# Example usage
nums = [5, 2, 3, 1]
print(sortArray(nums))  # Output: [1, 2, 3, 5]


# ## Answer 4

# In[7]:


def moveZeroes(nums):
    n = len(nums)
    next_non_zero = 0

    for i in range(n):
        if nums[i] != 0:
            nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
            next_non_zero += 1

# Example usage
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
moveZeroes(arr)
print(arr)  # Output: [1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0]


# ## Answer 5

# In[8]:


def rearrangeAlternating(nums):
    n = len(nums)
    # Partition the array into two groups: positive and negative
    positive_idx = 0
    for i in range(n):
        if nums[i] > 0:
            nums[positive_idx], nums[i] = nums[i], nums[positive_idx]
            positive_idx += 1

    # Find the starting indices of positive and negative groups
    positive_start, negative_start = 0, positive_idx

    # Merge the two groups back in an alternating fashion
    while negative_start < n and positive_start < negative_start and nums[positive_start] < 0:
        nums[positive_start], nums[negative_start] = nums[negative_start], nums[positive_start]
        positive_start += 2
        negative_start += 1

# Example usage
arr = [1, 2, 3, -4, -1, 4]
rearrangeAlternating(arr)
print(arr)  # Output: [-4, 1, -1, 2, 3, 4]

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
rearrangeAlternating(arr)
print(arr)  # Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]


# ## Answer 6

# In[9]:


def mergeSortedArrays(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    merged = []
    i, j = 0, 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < n1:
        merged.append(arr1[i])
        i += 1

    while j < n2:
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
result = mergeSortedArrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 4, 5, 6, 8]

arr1 = [5, 8, 9]
arr2 = [4, 7, 8]
result = mergeSortedArrays(arr1, arr2)
print(result)  # Output: [4, 5, 7, 8, 8, 9]


# ## Answer 7

# In[10]:


def intersection(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    # Find the common elements using the intersection of sets
    common_elements = set_nums1.intersection(set_nums2)

    # Convert the set to a list to return the result
    return list(common_elements)

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection(nums1, nums2)
print(result)  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersection(nums1, nums2)
print(result)  # Output: [9, 4]


# ## Answer 8

# In[11]:


def intersect(nums1, nums2):
    # Create dictionaries to count occurrences of elements in nums1 and nums2
    count_nums1 = {}
    count_nums2 = {}

    # Count occurrences in nums1
    for num in nums1:
        count_nums1[num] = count_nums1.get(num, 0) + 1

    # Count occurrences in nums2
    for num in nums2:
        count_nums2[num] = count_nums2.get(num, 0) + 1

    # Find common elements based on the minimum count of occurrences
    common_elements = []
    for num in count_nums1.keys():
        if num in count_nums2:
            common_occurrences = min(count_nums1[num], count_nums2[num])
            common_elements.extend([num] * common_occurrences)

    return common_elements

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)  # Output: [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersect(nums1, nums2)
print(result)  # Output: [4, 9]


# In[ ]:




