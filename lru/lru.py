"""
This script implements a LRU cache with variable size
POSSIBLE PROBLEMS WITH THIS IMPLEMENTATION:
    1. remove method from the linked list is based on value, not index. It will
    always remove the first found element from the list with the given value.
    Question: Is this relevant? Since if you might have repeated elements, when
    removing one of them it won't matter which one.
"""
import double_linked_list

class lru_cache(object):
    """
    LRU cache: store the most recently used item at the end and the least used
    one at the beginning.
    Here, I will use two data structures:
        - A hash table, to give O(1) access time to the cache
        - A doubly linked list, in order to remove items from the cache in an
          optimal way, with O(n) search time.
    """
    def __init__(self, size):
        self.cache_size = size
        self.cache      = {}
        self.cache_vals = double_linked_list.DoubleLinkedList()

    def set(self, key, data):
        # Check if the hash table already has that item stored. If it does,
        # simply update the given value by updating the node.data variable.
        # This is done by accessing the node via the hash table
        if self.cache.has_key(key):
            node = self.cache[key]

            # Now that we updated the node, it becomes the Most Recently used,
            # so we need to move it to the end of the list (the LRU is always
            # the HEAD, the MRU is always the TAIL
            self.cache_vals.remove(node)
            self.cache_vals.insert(node)
        else:
            # If the item is not on the hash table, it means we are dealing with
            # a new element. In order to add a new element, we need to check if
            # the cache has remaining space. If it doesn't, we flush the LRU
            # element out of the cache and add the new element as the new MRU
            # one.
            self.flush()
            node = double_linked_list.Node()

            # Update node pointer information
            node = self.cache_vals.insert(node)

            # Add it to the hash table
            self.cache[key] = node

            self.size += 1

    def get(self, key):
        if self.cache.has_key(key):
            node = self.cache[key]
            self.cache_vals.remove(node)
            self.cache_vals.insert(node)
            return node.data
        else:
            return -1

    def flush(self):
        if self.cache_vals.size() >= self.size:
            node = self.cache_vals.remove(self.cache_vals.head.data)
            del self.cache[node.key]

    def display(self):
        self.cache_vals.show()

