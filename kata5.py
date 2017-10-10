
file = open("word.txt")
text = file.read().strip().split()


while True:
    print "Type exit when you completed on entering the string"
    s = raw_input("Enter a string: ")
    if s == "":
        continue

    if s =="exit":
        break

    if s in text:
        print("This String is already in the list")


    else:
        print("No such string found,try again")
        file = open("word.txt","a")
        file.write("\n")
        file.write(s)
        print "This word was added to the list"
        continue

file.close()