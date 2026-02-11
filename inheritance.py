
#Parent Class/Siuper Class/Base Class
class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")



class Cat:
    def meow(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")


class Donkey:
    hasTail = True

    def move(self):
        print("Donkey is moving")


a = Animal()

c = Cat()

d = Donkey()