
first = int(input("Enter first number :"))
second = int(input("Enter second number :"))
third = int(input("Enter third number :"))

if first > second and first > third:
    print(first,"is the largest number")

elif second > first and second > third:
    print(second,"is the largest number")

elif third > first and third > second:
    print(third,"is the largest number")