import random

class Dog:
    info = "A furry domestic animal"
    
    # The init function is called everytime we call the Dog object
    def __init__(self, name): # we can also use our own varible in the init function
        print("I am alive!")
        self.lucky_number = random.randint(1, 10) # This is an instance variable accessed by the keyword "self"
        self.name = name

print(Dog.info)

# # creating an instance of the class Dog, we need to use the same name as the class
# Dog()
# Dog()
# Dog() # each of these objects are different from each other, and for every object the init function is called

# Instance variables -  particular to an individual object or instance

# dog1 = Dog()
# dog2 = Dog()

# print(dog1.lucky_number)
# print(dog2.lucky_number)

# # creating a new instance variable after an object is created

# dog1.name = "Fido"

# print(dog1.name) # the variable can be accessed since it has been instantiated but we cannot use the variable name for dog2 without instantiating
# # print(dog2.name) -----> This throws an error, since the dog2 object has no variable name

dog3 = Dog("Tommy")
print(dog3.name)