'''

2. Write a program to print third, fifth and seventh element from a list using enumerate 
function.

'''
li = ["one",2,"third",4,"fifth",6,"seventh"]

for i,item in enumerate(li):
    if i == 2 or i == 4 or i == 6:
        print(item)