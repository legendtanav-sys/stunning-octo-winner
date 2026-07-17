#create class
class Veichle:

    #create init method
    def __init__(self,max_speed,mileage):

        #blind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
        #object creation
modelx = Veichle(240, 18)
        #access the variables init method
print("model max speed", modelx.max_speed)
print("model max speed", modelx.mileage)