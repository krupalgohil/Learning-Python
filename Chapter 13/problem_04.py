'''

4. Write a program to filter a list of numbers which are divisible by 5. 

'''

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,3,4,5,6,7,8,9,0,15,10,25,20]

f = list(filter(divisible5,a))
print(f)