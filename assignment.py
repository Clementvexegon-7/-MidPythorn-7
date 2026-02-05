#A python program that allows a user enter a random number
#And check if the number is even or odd

number = int(input("Enter a number to reveal its nature: "))

if number % 2 == 0:
        print(f"The number {number} is Even.")
else:
        print(f"The number {number} is Odd.")


