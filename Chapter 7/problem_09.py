'''
print : 

* * * 
*   *   for n = 3 
* * *  

'''

n=5

for i in range(1,n+1):
    if(i == 1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")
   