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

dog2 = Dog("Tony", "German Shephard", "True")

dog3 = Dog("Ann", "Siberian Husky", "True")