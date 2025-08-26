'''


1. Create a class (2-D vector) and use it to create another class representing a 3-D 
vector. 


'''
class twod:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def print(self):
        print(f"the vactor is {self.i}i + {self.j}j")
    
class threed(twod):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def print(self):
        print(f"the vactor is {self.i}i + {self.j}j + {self.k}k")

a = twod(1, 2)
a.print()
b = threed(5, 2, 3)
b.print()