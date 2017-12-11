#kata04_Data_munging. To display the minimum temperature of each day. http://codekata.com/kata/kata04-data-munging/
print("DISPLAYING THE MINIMUM TEMPERATURE OF THE EACH DAY ")

with open("weather.dat", "r") as f:
    data = f.readlines()

for line in data:
    words=line.split()
    #print words
    a=[]
    for i in range(len(words)):
        a = words[0]

    print("Day:",a)

    for j in range(len(words)):
        b =words[2]

    print("Minimum Temperature:",b)
    print(" ")
