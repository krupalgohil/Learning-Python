'''

4. Add a static method in problem 2, to greet the user with hello. 

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
    @staticmethod
    def greet():
        print("hiii there")

a=calculator(4)
a.greet()
a.squre()
a.cube()
a.squreroot()