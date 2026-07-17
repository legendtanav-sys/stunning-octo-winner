#create class
class Parrot:
    #class attribute
    species = "bird"
    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #institiate the parrot class
        blu = Parrot("blu", 10)
        woo = Parrot("woo", 15)

#access class  attributes
print("blu is a {} ".format("blu species"))
print("woo is also a {} ".format("woo species"))