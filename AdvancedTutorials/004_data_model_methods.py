
# Documentation
# https://docs.python.org/3/reference/datamodel.html
#
#

class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self): # like override (print)
        return f"Person( {self.name} )"
    
    def __mul__(self,x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        
        self.name = (self.name + " ") * x
        
    def __call__(self, y):
        print("called this function", y)
        
    def __len__(self):
        return len(self.name)
    
    
        
p = Person("Tim")
print(p)

print("------------------------------------")

p * 4
print(p)

print("------------------------------------")

p("David")

print("------------------------------------")

print(len(p))

print("------------------------------------")
