#kata15-A_Diversion http://codekata.com/kata/kata15-a-diversion/
word="011"
count=1
length=""
for i in range(1,len(word)):
    if word[i-1]==word[i]:
       count+=1
    else :
        length += word[i-1]+" repeats "+str(count)+", "
        count=1
length += (word[i]+" repeats "+str(count))
print (length)
if(word[i]==1 and word[i+1]==1):
    print("Hi")