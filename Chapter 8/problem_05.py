# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 

def pattern(n):
    # for i in range(0,n):   
    #     star = (n-i)
    #     print("*" * star)
    
    # recursively
    
    if(n==0):             
        return
    print("*" * n)
    pattern(n-1)

    

print(pattern(5))    