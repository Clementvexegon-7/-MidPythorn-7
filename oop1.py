class Dog:

    def __init__(self,name,breed,hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur


    def bark(self):
        print("Woof!! Woof!!")

    def locomotive(self):
        print("Dog is walking")

dog1 = Dog("JJ", "Bulldog", "True")
print(dog1.name, dog1.breed, dog1.hasFur,
      dog1.bark)

dog2 = Dog("Tony", "German Shephard", "True")
print(dog2.name, dog2.breed, dog2.hasFur,
      dog2.locomotive)


dog3 = Dog("Ann", "Siberian Husky", "True")
print(dog3.name, dog3.breed, dog3.hasFur,
      dog3.bark)
