"""
Simple implementation of a double linked list
(based on http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/)
"""

class Node(object):
    """
    Simple linked list with two pointers and a storage for value
    """
    def __init__(self):
        self.data = None
        self.prev  = None
        self.next  = None

class DoubleLinkedList(object):
    """
    Double linked list class. Implements addition, removal and display methods
    """
    head = None
    tail = None
    size = 0

    def insert(self, node):
        # treat empy list case
        if self.head is None:
            self.head = self.tail = node
        # here the list already has at least one item
        else:
            # tail pointer walks the list. Point the 'prev' pointer from the new
            # node to the tail pointer
            node.prev = self.tail
            node.next = None

            # again, tail pointer points to the current last element of the
            # list, so we need to update it's next pointer to point to the new
            # node to be added
            self.tail.next = node

            # Finally, update the tail pointer to point to the most recently
            # added element
            self.tail = node
        self.size += 1
        return node

    def remove(set, node):
        """
        Removes an element from the list based on a given value
        """
        if self.size == 1:
            self.head = self.tail = None
        else:
            if node.prev is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
            else:
                self.head = node.next
                node.next.prev = None
                self.size -= 1
            return node
        return None

    def show(self):
        curr_node = self.head
        while curr_node.data is not None:
            print curr_node.data,
            curr_node = curr_node.next

    def size(self):
        return self.size

