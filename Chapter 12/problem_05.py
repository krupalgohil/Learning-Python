'''

5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

'''

n = 6 
n = 7
table = [n*i for i in range(1,11)]
print(table)

with open("table.txt","w") as f:
    f.write(str(table) + "\n") 