'''

5. Write a program to find the maximum of the numbers in a list using the reduce 
function. 

'''
from functools import reduce
l = [112,2,3,45,6,77,88,56,24,36,78,27]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))




