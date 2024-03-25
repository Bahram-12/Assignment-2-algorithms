#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sort_merge(sequence, depth=0):
    # Check if sequence is a single element or empty
    if len(sequence) <= 1:
        return sequence

    # Split the sequence in half and apply sort_merge recursively
    middle = len(sequence) // 2
    left_section = sort_merge(sequence[:middle], depth+1)
    right_section = sort_merge(sequence[middle:], depth+1)

    # Combine the sorted sections
    combined = combine(left_section, right_section, depth)

    # If at the initial call level, display the sorted sequence
    if depth == 0:
        print(f"Sorted sequence: {combined}")
    return combined

def combine(left, right, depth):
    combined_sequence = []
    index_left = index_right = 0

    # Display the merging process at the current depth
    print(f"{'  '*depth}Combining {left} and {right}")

    # Merge elements from left and right in a sorted manner
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            combined_sequence.append(left[index_left])
            index_left += 1
        else:
            combined_sequence.append(right[index_right])
            index_right += 1

    # Add remaining elements from left and right
    combined_sequence.extend(left[index_left:])
    combined_sequence.extend(right[index_right:])

    # Display the combined sequence
    print(f"{'  '*depth}Combined result: {combined_sequence}")
    return combined_sequence

# Demonstration
sequence = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Initial sequence:", sequence)
sort_merge(sequence)


# In[ ]:




