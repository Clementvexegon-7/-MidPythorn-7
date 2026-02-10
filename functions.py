#Functions/Methods - A block of codes used to perform a task
from datatypes import age

#1. Standard -  Library/Inbuilt Functions - Already exists

y = max(56, 67, 345, 213, 5666, 6788, 2344)
print(y)

x = min(56, 67, 345, 213)
print(x)

#2. User - Defined Functions
def school():
    print("eMobilis")

school() #Calling a function

#Parameters/Variables
def multiply(x, y):
    print(x * y)

multiply(34, 18)


#Fullname position age gender

def work (Fullname, position, age, gender ) :
    print(Fullname, position, age, gender )

work("Lewis Halimton", "F1 racer", "34yrs", "male")
print()
work("Akira Toriyama", "Mangaka", "64yrs", "male")
print()
work("Evangeline Nyanguthie", "Doctor", "42yrs", "female")
print()
work("Glory Akinyi", "Developer", "30yrs", "female")
print()



#Python program to diplay details of 5 employeees at eMobilis

#Use a user-defined functions with the help of paramrters and arguments

#Details - Fullnames, Position, age, gender