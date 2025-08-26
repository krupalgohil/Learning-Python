'''
2. Write a class “Calculator” capable of finding square, cube and square root of a 
number. 

'''
class calculator:
    def __init__(self,n):
        self.n = n
    def squre(self):
        print(f"squre of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"cube of {self.n} is {self.n*self.n*self.n}")
    def squreroot(self):
        print(f"squreroot of {self.n} is {self.n**1/2}")

a=calculator(4)
a.squre()
a.cube()
a.squreroot()