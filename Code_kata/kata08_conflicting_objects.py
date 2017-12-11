#Implementation of kata-08 http://codekata.com/kata/kata08-conflicting-objectives/
import time
"""The first time, make program as readable as you can make it."""
start_time = time.time()
def check(str1,str2):
    datafile = open("words.txt").read()
    word = str1+str2
    print word
    if word in datafile:
        return True
    else:
        return False

if check("al", "bums"):
    print "word exist"
else:
    print "word doesn't exist"
print "The first way of implementation takes "
print("--- %s seconds ---" % (time.time()-start_time))
print ""

"""The second time, optimize the program to run fast fast as you can make it."""
start_time = time.time()
str1 = "al"
str2 = "bums"
join = str1+str2
print join

if join in open("words.txt").read():
    print "word exist"
else:
    print "word doesn't exist"
print "The second way of implementation takes "
print("--- %s seconds ---" % (time.time()-start_time))
print ""

"""The third time, write as extendible a program as you can."""
start_time = time.time()
def check():
    datafile = file("words.txt")
    str1 = "al"
    str2 = "bums"
    word = str1+str2
    print word
    for line in datafile:
        if word in line:
            return True
    return False

if check():
    print "word exist"
else:
    print "word doesn't exist"
print "The third way of implementation takes "
print("--- %s seconds ---" % (time.time()-start_time))
print ""