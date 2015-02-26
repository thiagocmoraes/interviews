"""
Find all permutations of a string
"""

# To be used in the easy answer
import itertools

# Simple solution
def permutations(head, tail=''):
    if len(head) == 0:
        print tail
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])

# Create a generator so we don't use too much memory
def permutations2(word):
    if len(word) <= 1:
        yield word
    else:
        for i in range(len(word)):
            for perm in permutations(word[1:]):
                yield perm[:i] + word[0:1] + perm[i:]

# Using python awesomeness
def permutations3(word):
    return itertools.permutations(word)
    
# thiago's solution
def permute(lst, n):
    # you yield tuples of values for permutations of lst elements in groups of n elements 
    for i in range(len(lst)):
        if n == 1:
            yield (lst[i],) #returns a tuple with the element
        else:
            # get a permute of all elements EXCEPT the one you're at, taken in smaller groups (n-1)
            for elem in permute(lst[:i] + lst[i+1:], n-1): 
                # for each element of this smaller permutation, you add you current element in front of it
                yield (lst[i],) + elem
                
def permute_trace(lst, n):
    for i in range(len(lst)):
        if n == 1:
            print 'base', (lst[i],)
            yield (lst[i],)
        else:
            for elem in permute(lst[:i] + lst[i+1:], n-1):
                print 'list + elem', (lst[i],) + elem
                yield (lst[i],) + elem
            print

print 'thiago solution', list(permute('abc', 3))
print 'follow the trace\n', list(permute_trace('abc', 3))


# How to use it:
for p in permutations("abc"):
    print(p)

for p in permutations2("abc"):
    print "".join(i)

for p in permutations3("abc"):
    print "".join(i)

