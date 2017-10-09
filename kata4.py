
print "DISPLAYING THE MINIMUM TEMPERATURE OF THE EACH DAY "


def my_min_function(somelist):
    min_value = None
    for value in somelist:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


with open("weather.dat", "r") as f:
    data = f.readlines()

for line in data:
    firstwords=line.split()
    #print firstwords
    a=[]
    for i in range(len(firstwords)):
        a = firstwords[0]

    print "Day:",a

    for j in range(len(firstwords)):
        b =firstwords[2]

    print "Minimum Temperature:",b
    print " "



print my_min_function(a)