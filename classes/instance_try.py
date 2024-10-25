# Whatever your previous class was, make an instance of it and add an instance variable to it 

class Laptop:
    def __init__(self, name):
        self.name = name

laptop1 = Laptop("MSI Modern 14 B4MW")

print(laptop1.name)