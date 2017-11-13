#Sorting the characters http://codekata.com/kata/kata11-sorting-it-out/"
# Get the sentence as input
print("Enter 'x' for exit.")
string = input("Enter any string: ")
if string == 'x':
	exit()
else:
	newstr = string
    # remove the punctuations and spaces in the sentence
	print("\nRemoving punctuations and spaces from the given string...")
	punctuations = '''" "!@#$%^&*()-+=[]{};:'"\,<>./?_~'''
	for x in string.lower():
		if x in punctuations:
			newstr = newstr.replace(x,"")
	print(newstr,"\n")

#converting the all letters into lower case
print("Converting the uppercases into lower case")
a=newstr.lower()
print(a,"\n")

#Arrange the words in alphabetical order
print("Arranging the word in alphabetical order")
b=sorted(a)
print("".join(b))