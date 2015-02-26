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
        self.next = next


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
            self.head = self.tail = new_node
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

    # Given the pointer/reference to the head of a singly linked list, reverse
    # it and return the pointer to the head of the reversed linked list
    def reverse(self):
        if None == self.head or None == self.head.next:
            return self.head
        else:
            p1 = self.head
            p2 = self.head.next
            p3 = self.head.next

            p1.next = None

            while p2.next is not None:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            p2.next = p1
            return p2


s = SingleLinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.show()

r = s.reverse
while True:
    print r.value, " -> ",
    r = r.next
    if r.next is None:
        print r.value, " -> ", None
        break
