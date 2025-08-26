'''

6. Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. 

'''
# Example of using "harry" instead of "self"

class Student:
    def __init__(harry, name, rollno):   # here "harry" is used instead of self
        harry.name = name
        harry.rollno = rollno

    def display(harry):
        print(f"Name: {harry.name}, Roll No: {harry.rollno}")

# Creating objects
s1 = Student("Krupal", 101)
s2 = Student("Ravi", 102)

# Calling method
s1.display()
s2.display()
