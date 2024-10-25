# In your previous class, add a method that uses one of the instance variables

class Laptop:
    def __init__(self, name):
        self.name = name
        self.build_year = 2020

    def laptop_name(self):
        print(f"The laptop is {self.name} and the build year is {self.build_year}")

laptop1 = Laptop("MSI B4MW")
laptop2 = Laptop("Dell Inspiron")

laptop2.build_year = 2023 # overriding the initialized build year for a certain class object
laptop1.laptop_name()
laptop2.laptop_name()