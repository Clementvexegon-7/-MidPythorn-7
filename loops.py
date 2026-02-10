#while Loop
from itertools import count

from variables import language

number = 100
while number <= 105:
    print(number)
    number += 1


#Program 2
count = 10
while count >= 5:
    print("Number", count)
    count -= 1

print()


#For Loop
for num in range(100, 106,):
    print(num)

languages = ["Python", "Java", "Javascript"]

for lang in languages:
    print(lang)

#Break and continue statements