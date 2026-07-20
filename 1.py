# create class
class IOString():

    # constructor
    def __init__(self):
        self.str1 = "" 
        #function i dont know what to name it
    def get_string(self):
            self.str1 = input("Enter string")

    # i dont know but it is a function!!!
    def print_string(self):
        print("result is :",self.str1.upper())
        #create object
str1 = IOString()

#call functions
str1.get_string()
str1.print_string()