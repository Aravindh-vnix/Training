print "DISPLAYING THE MINIMUM TEMPERATURE OF THE EACH DAY "


def min_function(temperatures):
    min_value = None
    for value in temperatures:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


with open("weather.dat", "r") as f:
    data = f.readlines()

for line in data:
    words=line.split()
    #print words
    a=[]
    for i in range(len(words)):
        a = words[0]

    print "Day:",a

    for j in range(len(words)):
        b =words[2]

    print "Minimum Temperature:",b
    print " "



print min_function(a)
