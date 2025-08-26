'''

4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the ‘ZeroDivisionError’. 

'''

a=3
b=0
try:
    print(a/b)
except ZeroDivisionError as d:
    print("infinite")