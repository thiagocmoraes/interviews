"""
Simple implementation of a double linked list
"""

class Node(object):
    """
    Simple linked list with two pointers and a storage for value
    """
    def __init__(self):
        self.value = None
        self.prev  = None
        self.next  = None

class DoubleLinkedList(object):
    """
    Double linked list class. Implements addition, removal and display methods
    """
    head = None
    tail = None

    def add(self, data):
        # Create new node with given value
        new_node = Node(data, None, None)

        # treat empy list case
        if self.head is None:
            self.head = self.tail = new_node
        # here the list already has at least one item
        else:
            # tail pointer walks the list. Point the 'prev' pointer from the new
            # node to the tail pointer
            new_node.prev = self.tail
            new_node.next = None

            # again, tail pointer points to the current last element of the
            # list, so we need to update it's next pointer to point to the new
            # node to be added
            self.tail.next = new_node

            # Finally, update the tail pointer to point to the most recently
            # added element
            self.tail = new_node

    def remove(set, node_val):
        """
        Removes an element from the list based on a given value
        """
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == node_val:
                # Check if we are dealing with the first element
                if curr_node.prev is not None:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                else:
                    self.head = curr_node.next
                    curr_node.next.prev = None
            curr_node = curr_node.next

    def show(self):
        curr_node = self.head
        while curr_node.value is not None:
            print curr_node.value,
            curr_node = curr_node.next
