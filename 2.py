# create class
class EMPLOYEE:
    #initializinggggg
    def __init__(self):
        
    # calling destructor
            def __del__(self):
                print("destructor called")
def create_obj():
     print('making object...')
     obj = EMPLOYEE
     print('function end')
     return obj

print('calling create_obj() function...')
obj = create_obj
print('program end.')
del obj