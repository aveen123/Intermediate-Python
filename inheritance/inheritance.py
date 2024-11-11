import random 

class Animal:
    info = "a living organism that feeds on organic matter."

    def __init__(self):
        print("An animal is created.")

class Dog(Animal):
    info = "a domesticated carnivorous animal."

    def __init__(self, name):

        super().__init__()
        print("A dog is created.")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"Woof! My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("Fido")

