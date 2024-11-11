# In your previous class, add a parent or a child class

class Media:
    def __init__(self, name):
        print("This is the init function of MEDIA.") 
        self.name = name


class Laptop(Media):
    def __init__(self, name):
        super().__init__(name)
        print("This is the init function of LAPTOP.")

laptop1 = Laptop("MSI")
