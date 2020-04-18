# binary search tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def print(self, traversal_type):
        if traversal_type == "preOrder":
            return self.pre_Order(tree.root, "")
        else:
            print("traversal not supported")
            return False

    def pre_Order(self, start, traversal):
        """start : will store the updated root
        traversal : will store the string and print out at last
        depth first search : root -> left -> right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_Order(start.left, traversal)
            traversal = self.pre_Order(start.right, traversal)
        return traversal


#                1
#              /   \
#             2     3
#            / \   / \
#           4   5 6   7

#   set up tree

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# three ways to search : pre order, post order , in order
# two ways to implement : depth first , breadth first

print(tree.print("preOrder"))

