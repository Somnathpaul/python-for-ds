# binary search tree 
class Node(object):
    def init (self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BST(object):
    def init (self, root):
        self.root = Node(root)
    
    def pre_Order (self, start, traversal):
        # root -> left -> right
        

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


