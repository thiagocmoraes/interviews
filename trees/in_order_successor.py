"""
Inorder successor of a node in a Binary Search Tree is the next node inorder
traversal. Write a method to find inorder successor of a given value "d" in a
BST
"""

def find_min(root):
    if None == root:
        return root

    while root.left != None:
        root = root.left

    return root

def inorder(root, d ):
    if None == root:
        return root

    successor = None

    while root != None:
        if root.data < d:
            successor = root
            root = root.left
        else:
            if root.right != None:
                successor = find_min(root.right)
                break
            return successor

