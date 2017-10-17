print "RULES"
print "1.Change the first form of word into final form of word."
print "2.Every word you are entering should be in a same length."
print "3.When you are entering the next word that should be replaced by only one letter of previous word and that must be a legal word."
print "4.You have an maximum of 6 attempts and minimum of 4 attempts"
print " "

first = raw_input("Enter the first form of word:")
print "The first form of word is ", first
final = raw_input("Enter the last form of word:")
print "The last form of word is ", final

file = open("words.txt", "r")
if first and final in open("words.txt").read() and len(first) == len(final):
    print " "
    print "Now change the word", first+" into",final
    second = raw_input("Enter second form of the word:")
    print second
    if second in open("words.txt").read() and len(first) == len(second):
        third = raw_input("Enter third form of the word:")
        print third
        if third in open("words.txt").read() and len(second) == len(third):
            fourth = raw_input("Enter the fourth form of the word:")
            print fourth
            if fourth in open("words.txt").read() and len(third) == len(fourth) and final == fourth:
                print "Matched with last form of word"
            else:
                fifth = raw_input("Enter the fifth form of word:")
                print fifth
                if fifth in open("words.txt").read() and len(fourth) == len(fifth) and final == fifth:
                    print "Matched with last form of word"
                else:
                    sixth = raw_input("Enter the sixth word:")
                    print sixth
                    if sixth in open("words.txt").read() and len(fifth) == len(sixth) and final == sixth:
                        print "Matched with last form of word"
                    else:
                        print "You are not found the word until the last attempt"
        else:
            print "You entered an illegal word"
    else:
        print "You entered an illegal word"
else:
    print "You Entered an illegal word."