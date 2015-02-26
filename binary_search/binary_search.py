"""
Write a code in any language to implement binary search algorithm
"""

def binary_search(haystack, needle):
    low = 0
    high = len(haystack)-1
    while (low <= high):
        s = (low + high)/2
        if haystack[s] == needle:
            return s
        if haystack[s] > needle:
            high = s
        if haystack[s] < needle:
            low = s

# Test cases
haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
needle = 4
result = binary_search(haystack, needle)
print "Expected Result: Index 3"
print result

