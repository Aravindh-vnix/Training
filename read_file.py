
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
   # print firstwords
    a=[]
    for i in range(len(firstwords)):
         a= firstwords[3]
    print a

print my_min_function(a)

