""" This script implements a LRU cache with variable size
"""

class lru_cache(object):
    """
    LRU cache: store the most recently used item at the end and the least used
    one at the beginning.
    """
    def __init__(self, size):
        self.cache_size = size
        self.cache      = {}
        self.cache_vals = dlink_list()

    def set(self, key, item):
        if self.cache.has_key(key):
            node = self.cache[key]
            node.data = value
            self.cache_vals.remove(node)
            self.cache_vals.insert_at_tail(node)
        else:
            self.evict()
            node = list_node(key, value)
            self.cache.insert_at_tail(node)
            self.cache[key] = node

    def get(self, key):
        if self.cache.has_key(key):
            node = self.cache[key]
            self.cache_vals.remove(node)
            self.cache_vals.insert_at_tail(node)
            return node.data
        else:
            return -1

    def evict(self):
        if self.cache_vals.size >= self.size:
            node = self.cache_vals.remove_head()
            del self.cache[node.key]

    def print_cache(self):
        node = sef.cache_vals.head
        while node != None:
            print str(node.key) + " " + str(node.data) + ", "
            node = node.next


    def get(self, value):
        self.cache.remove(value)
        self.cache.append(value)

    def display(self):
        print(self.cache)

if __name__ == "__main__":
    # Initialize cache
    lru = lru_cache(5)

    # Add items to cache
    lru.set('a')
    lru.set('b')
    lru.set('c')
    lru.set('d')
    lru.set('e')

    lru.display()

    # change MRU
    lru.get(0)
    lru.display()

    lru.get(2)
    lru.display()

    # Add new item
    lru.set('f')

    lru.display()

