"""
Simple implementation of a singly linked list
(based on http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/)
"""
import copy

class Node(object):
    """
    Node base class
    """
    def __init__(self):
        self.value = None
        self.next  = None


class SingleLinkedList(object):
    """
    Singly linked list class. Implements addition, removal and display methods
    """
    head = None
    tail = None

    def append(self, node):
        # Check if list is empty
        if self.head is None:
            self.head = self.tail =  node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node):
        prev_node = self.head
        curr_node = self.head.next
        while prev_node is not None:
            if curr_node.next == node.next:
                if curr_node.next is not None:
                    prev_node.next = curr_node.next
                else:
"single_linked_list.py" 76L, 1866C
            curr_node = curr_node.next
            # Is this correct?
            # curr_node = curr_node.next
            # prev_node = prev_node.next


    def append(self, node):$
            prev_node = curr_node
            curr_node = curr_node.next
        return node


    def show(self):
        node = self.head
        while node.next is not None:
            print node.value,
            node = node.next
        print None

    # Exercise: Given the pointer/reference to the head of a singly linked list,
    # reverse it and return the pointer/reference to the head of the reversed
    # linked list
    def reverse(self, single_list):
        rev = SingleLinkedList()
        li = copy.copy(single_list)
        while li is not None:
            node = li.remove(li.tail)
            rev.append(node)

s = SingleLinkedList()
s.append(31)
s.append(2)
s.append(3)
s.append(4)


s.show()
s.remove(31)
s.remove(3)
s.remove(2)
s.show()
