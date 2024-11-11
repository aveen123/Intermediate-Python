print ("before")
try:
    4/0
    # print(name)
except NameError as e:
    print("This was a name issue")
    print(e)
except ZeroDivisionError as e:
    print("Can't divide by 0")
    print(e)
except Exception as e:
    print("Something went wrong.")
    print(e)

class CheeseError(Exception):
    pass

def upper_fun(word):
    if len(word) <=0:
        raise CheeseError("The word has to have at least 1 letter !!")
    return word.upper()

print(upper_fun(""))
print("after")