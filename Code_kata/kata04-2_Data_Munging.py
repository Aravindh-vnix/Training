#kata04_data_Munging http://codekata.com/kata/kata04-data-munging/
with open("football.dat", "r") as f:
    data = f.readlines()

for line in data:
    words=line.split()
    #print words
    for i in range(len(words)):
        a = words[1]
    print "Team name:",a

    for j in range(len(words)):
        b =words[6]
    print "Total goals scored:",b

    for k in range(len(words)):
        c =words[7]
    print "Total goals against them:", c
    print " "

