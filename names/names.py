import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
search_tree = BinarySearchTree(names_1[0])  # put in the first name to start
# Replace the nested for loops below with your improvements
for name_1 in names_1:  # loop though each name in in names_1.txt
    # create a binary search tree out of those names
    search_tree.insert(name_1)
for name_2 in names_2:  # seperate loop though names_2.txt
    # seach the binary search tree with each name in names_2.txt
    if search_tree.contains(name_2):
        # if it there is a match from names_2 to names_1, append the name to the array
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# OLD CODE  == O(n^2)
# NEW CODE  == O(n log n)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
