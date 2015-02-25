""" This script counts how many unique words there are in a file and how many
times each word ocurred
"""

total_words = {}

def read_file():
    """quick and sirty read a file """
    try: 
        f = open("words.txt")
        return f
    except IOError:
        print "File not found"

def check_words(f):
    for line in f:
        line = line.strip()
        if total_words.has_key(line):
            total_words[line] += 1
        else:
            total_words[line]  = 1

def uniques():
    for key in total_words.keys():
        if total_words[key] == 1:
            print key
        
def repeated():
    for key in total_words.keys():
        s = str(key) + ": " + str(total_words[key])
        print s

if __name__ == "__main__":
    w = read_file()
    check_words(w)
    uniques()
    repeated()

