# Linked Lists in a nutshell

(souce:
http://www.quora.com/Data-Structures-When-is-a-singly-linked-list-more-useful-than-a-doubly-linked-list-and-vice-versa)

## Singly linked list over double linked list:

### Pros:
1. Less memory requirement.
2. It only needs to keep forward pointer/referencing in place.
3. Singly linked list are persistent data structure.
    3.1 http://en.wikipedia.org/wiki/Persistent_data_structure#Linked_lists
4.  A singly linked list is often used as a stack (or last in first out queue
(LIFO)) because adding a new first element, removing the existing first element,
and examining the first element are very fast O(1) operations.

### Cons:
1. In general, to remove a node from the list, you have to change the next
pointer of the node that appears before the node to remove so that it no longer
points to the node to remove. In the case when you have a pointer to the node
to be deleted. You have to start at the beginning of the list, iterate it all
over  till you find the node that comes just before the node to be deleted. This
takes time O(n), so the runtime for the remove step is O(n) in the worst case.

2. Provides Sequential access in one direction. What if you want access in both
directions, make it a DLL.

## Doubly linked list over Singly linked list:

### Pros:
1. To remove a node when a pointer is given to that node, double linked list
requires O(1) in worst case.
2. Provides sequential access in both direction.

### Cons:
1. More memory requirement (if it is not a xored one A Memory-Efficient Doubly
Linked List, XOR linked list). Requires two pointers previous, and next as it
is a two way.
2. It needs to keep both forward and backward pointers in place.
3. Double linked list do not adapt well with a persistent setting.

## Cycles in linked lists

(source: http://ostermiller.org/find_loop_singly_linked_list.html)

If a linked list has a cycle:

 - The malformed linked list has no end (no node ever has a null next_node pointer)
 - The malformed linked list contains two links to some node
 - Iterating through the malformed linked list will yield all nodes in the loop
   multiple times
