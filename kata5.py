
import os



while True:
    print ""
    print "Type 'stop' when you stopped adding the string"
    s = raw_input("Enter the string:")
    if s=="stop":
        break

    with open("word.txt" ,"r+") as f:
        line_found = any(s in line for line in f)
        print "This word is Exist"

        if not line_found:
            f.seek(0 ,os.SEEK_END)
            f.write(s)
            f.write("\n")
            print "Now only Added to the file. check the file now"

