'''

1. Create a class “Programmer” for storing information of few programmers 
working at Microsoft. 

'''

class programmer:
    company = "microsoft"
    def __init__(self,name,lan,salary):
        self.name = name
        self.lan = lan
        self.salary = salary

p = programmer("krupal","python",200000)   
print(p.name,p.salary,p.lan)    
p = programmer("naksh","python",200000)   
print(p.name,p.salary,p.lan)      

