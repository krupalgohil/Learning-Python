# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 
# F:\python DA\Chapter 9\problem_01.txt
f= open("chapter 9\\problem_01.txt")
content = f.read()
if("twinkle" in content):
    print("true")
else:
    print("false")    
f.close()    