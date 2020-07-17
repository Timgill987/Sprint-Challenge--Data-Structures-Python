import time
from BST import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# 0(n^2)
# for name_1 in names_1:0(n)
#     for name_2 in names_2: 0(n)
#         if name_1 == name_2: 0(1)
#             duplicates.append(name_1) 0(1)

bst = None #0(1)
for name_1 in names_1: #0(n) # followed the bst tester
    if bst is None: #0(1)
        bst = BSTNode(name_1)#0(1)
    else:
        bst.insert(name_1) #0(log n)
#first loop 0(n log n)


for name_2 in names_2: #0(n)
    if bst.contains(name_2): #0(log n)
        duplicates.append(name_2) #0(1)
#0(n log n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
