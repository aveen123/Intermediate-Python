# A method is a function which is inside of a class

import random 

class Dog:
    info = "A furry domestic animal"

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name 

    def bark(self):
        print(f"woof! My name is {self.name} and my lucky number is {self.lucky_number}")

dog1 = Dog("Fido")
dog2 = Dog("Sarah")

dog1.bark()
dog2.bark()