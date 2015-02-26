"""
There are n steps in a hill. You stand on the top, you can climb down either one
step or two steps at a time. Find the number of paths by which you can reach the
bottom?
"""

#                              5
#                4                          3
#            3           2              2       1
#        2       1   1       0      1       0
#    1       0
#
# Easiest way: count the number of leaves

def steps(root):
    if None == root:
        return -1
    else:
        if root.left is None and root.right is None:
            return 1
        else:
            return steps(root.left) + steps(root.right)
            
