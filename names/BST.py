"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
​
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
on the BSTNode class
"""
from queue import Queue
from stack import Stack
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            # ADD LEFT LEAF
            if self.left is None:
                self.left = BSTNode(value) # new left leaf
            else:
                # Repeat the process on left subtree
                self.left.insert(value)
        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
                #ADD RIGHT LEAF
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        while self.right is not None:
            self = self.right
        return self.value
        # iterate through the nodes using a loop construct
# Call the function `fn` on the value of each node
    def for_each(self, fn):
        node = self
        fn(node.value)

        if node.left:
            node.left.for_each(fn)

        if node.right:
            node.right.for_each(fn)


    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(node) #L


        print(self.value) #N

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node) #R

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        #self.in_order_print(node)
        queue = Queue()
        queue.enqueue(node)

        while (queue.size  > 0):
            w = queue.dequeue()
            print(w.value)
            if w.left is not None:
                queue.enqueue(w.left)
            if w.right is not None:
                queue.enqueue(w.right)


            # #this is recursive
            # if node.left is not None:
            #     node.left.bft_print(node.left)

            # if node.right is not None:
            #     node.right.bft_print(node.right)


        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line"
        # for the nodes to "get in"

        # start by placing the root in the queue

        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item

        # place current item's left node in queue if not None
        # place current item's right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize an empty stack
        # push the root node onto the stack

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        # pop top item off the stack
        # print that item's value

        # if there is a right subtree
        # push right item onto the stack

        # if there is a left subtree
        # push left item onto the stack
        stack = Stack()
        stack.push(node)

        while (stack.size  > 0):
            w = stack.pop()
            print(w.value)
            if w.left is not None:
                stack.push(w.left)
            if w.right is not None:
                stack.push(w.right)



# Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        if self is None:
            return
        print(self.value) #N


        if self.left is not None:
            self.left.pre_order_dft(node.left) #L

        if self.right is not None:
            self.right.pre_order_dft(node.right) #R


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self is None:
            return

        if self.left is not None:
            self.left.post_order_dft(node.left) #L

        if self.right is not None:
            self.right.post_order_dft(node.right) #R

        print(self.value) #N

        pass