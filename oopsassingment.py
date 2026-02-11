# Task 1: Create the Class from datatypes import student


#Create a class called Student with the following attributes: fullname, course, age, feesPaid

# Student.py - A simple class to represent a student

class Student:


    def __init__(self, fullname, course, age, feesPaid):

        self.fullname = fullname
        self.course = course
        self.age = age
        self.feesPaid = feesPaid

    def display_info(self):

        # method to display the student's information nicely.

        print(f"Name: {self.fullname}")
        print(f"Course: {self.course}")
        print(f"Age: {self.age}")
        print(f"Fees Paid: ${self.feesPaid}")
        print("-" * 30)


# Example usage - How to create and use student objects:
if __name__ == "__main__":
    # Creating student objects (instances of the Student class)
    student1 = Student("Naruto Uzumaki", "Computer Science", 21, 5000.00)
    student2 = Student("Edward Elric", "Alchemy Engineering", 19, 4500.00)
    student3 = Student("Peter Parker", "Physics", 20, 6000.00)

    # Display their information
    print("=== Student Records ===\n")
    student1.display_info()
    student2.display_info()
    student3.display_info()

    # You can also access individual attributes
    print(f"{student1.fullname} is studying {student1.course}")











#Task 2: Create Multiple Objects
#Create at least three student objects from the same class with different values and display the same information