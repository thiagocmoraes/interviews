"""
Find all permutations of a string
"""

# To be used in the easy answer
import itertools

# Create a generator so we don't use too much memory
def permutations(word):
    if len(word) <= 1:
        yield word
    else:
        for i in range(len(word)):
            for perm in permutations(word[1:]):
                yield perm[:i] + word[0:1] + perm[i:]

# Using python awesomeness
def permutations2(word):
    return itertools.permutations(word)


# How to use it:
for p in permutations("abc"):
    print(p)

for p in permutations2("abc"):
    print "".join(i)

