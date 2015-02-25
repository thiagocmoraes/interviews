"""
Simple implementation of a singly linked list
(based on http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/)
"""
class Node(object):
    """
    Node base class
    """
    def __init__(self, value, next):
        self.value = value
        self.next  = next


class SingleLinkedList(object):
    """
    Singly linked list class. Implements addition, removal and display methods
    """
    head = None
    tail = None

    def append(self, value):
        # Check if list is empty
        new_node = Node(value, None)
        if self.head is None:
            self.head = self.tail =  new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        return new_node

    def remove(self, value):
        prev_node = self.head
        curr_node = self.head.next
        while curr_node.next is not None:
            if curr_node.value == value:
                if curr_node.next is not None:
                    prev_node.next = curr_node.next
                    return prev_node
                else:
                    self.head = curr_node.next
                    return self.head
            # Is this correct?
            # curr_node = curr_node.next
            # prev_node = prev_node.next
            prev_node = curr_node
            curr_node = curr_node.next
                
    def show(self):
        node = self.head
        while True:
            print node.value, " -> ",
            node = node.next
            if node.next is None:
                print node.value, " -> ", None
                break

