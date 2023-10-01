from collections import Counter

my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 4]

# Use Counter to count all elements and their occurrences
element_counts = Counter(my_list)

# Print the element counts
for element, count in element_counts.items():
    print(f"{element} appears {count} times in the list.")
