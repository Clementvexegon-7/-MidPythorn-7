age = 56 #Integer
length = 45.6 #Float
greeting = "Hello there" #String
hasFeathers = True #Boolean

#Data structures- Multiple values stored in one variable.
fruits = ["Banana", "Mango", "Pineapple"] # List - Ordered and changeable
courses = ["MIT", "Datascience", "Cybersecurity"] #array - Similar Datatypes
cars = ["Mercedes", "Ford", "Nissan", "G-Wagon", "Pagani" "Lamborghini"] #Tuple - Ordered and unchangeable
countries = {"Kenya", "Canada", "India", "Austria"} #Set - Unordered and unchangeable
student ={
    "firstname" : "Esther",
    "coures" : "MIT",
    "Age" : 19,
    "nationality" : "Kenya",
    "gender" : "Female"
}#Dictionary

print(age)
print("The length is", length)
print(fruits)
print(countries)
print(student)
print(student["nationality"])

#Typecasting - Converting one datatype to another.
print(float(age))
print(int(student))