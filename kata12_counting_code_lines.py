#Counting the total number of lines excluded with blank lines and comment lines. http://codekata.com/kata/kata13-counting-code-lines/
comment_lines=0
lines_count=0
with open ('word.txt','rb') as f:
    for line in f:
        li=line.strip()
        if li.startswith(b"#"):
            comment_lines += 1

        if line.strip():
            lines_count += 1

total=(lines_count-comment_lines)
print(total)
