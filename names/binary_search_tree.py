

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree

    def insert(self, value):
        if value < self.value:  # if value is smaller than node
            if self.left:  # if there is something to the left
                self.left.insert(value)  # if there is a node, then recurse
            else:
                # if there is no node, make a new leaf with value
                self.left = BinarySearchTree(value)  # base case
        # if value is greater or equal to node
        else:
            if self.right:  # check if there is something to the left
                self.right.insert(value)  # if there is, recurse
            else:
                # if there is no node, make new leaf with value
                self.right = BinarySearchTree(value)  # base case

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if current node contains value
        if self.value == target:
            return True
        # if current node is less than value
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)  # move right and recurse
            # if value is less
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
