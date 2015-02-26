"""
Mirror binary tree given the root node of the tree
"""

class Tree(object):
    def add(self):
        pass

    def remove(self):
        pass

    def traverse(self):
        pass

    # Do a depth first traversal and backtrack swapping the branches at each
    # level
    def mirror(self):
        if root == None:
            return root

        if root.left != None:
            mirror(root.left)

        if root.right != None:
            mirror(root.right)

        # Swap the nodes at current level
        tmp = root.left
        root.left = root.right
        root.right = tmp


