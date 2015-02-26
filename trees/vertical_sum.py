"""
Write a program to find the vertical sum of a binary tree
"""

from collections import deque

def vertical_sum(root):
    if root is None:
        return 0
    else:
        q = deque()
        q.append(root)
        q.append(None)
        res = 0

        # Here, we use a queue to store the elements in a given tree. We also
        # use None as a marker stored at the end of the queue. We start popping
        # items out of the queue until all is left is the marker on the left
        # side. When we read that, we know that we reached the end of an level.
        # We reset thre res variable and start on the queue again.
        while len(q) != 0:
            tmp = q.popleft()
            res += tmp.data

            if tmp.left != None:
                q.append(tmp.left)
            if tmp.right != None:
                q.append(tmp.right)
            if q[0] = None
                q.popleft()
                res = 0
            if len(q) != 0:
                q.append(None)
                
            




