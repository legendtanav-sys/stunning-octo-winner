#part 1 create a parent to create traits
class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eyecolor = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Color", self.eyecolor)
        print("Height (cm)",self.height_cm )
        
        #part 2 create the child that inherits from the family
class kid(FamilyMember):

    #part 3 give the kid his own details, styles etc
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)
        #part 4
        def show_traits(self):
            print("name", self.name)
            print("age", self.age)
            super().show_traits
            #part five
            def favorite_hobby(self,hobby):
                print(self.name, "loves", hobby)

                #pt 6
child = kid("maya", 10, "brown", 140)
#part 7
child.show_traits()
child.favorite_hobby("painting")

#part 8
print("is the kid a subclass of the family member???", issubclass(kid,FamilyMember))