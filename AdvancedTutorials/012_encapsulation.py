class Person:
    def __init__(self,name, age, gender):
        self.__name = name      # __name is a private attribute (__ is a naming convention of private attributes)
        self.__age = age        # __age is a private attribute
        self.__gender = gender  # 
    
    @property    # getter
    def Name(self):
        return self.__name
    
    @Name.setter # setter
    def Name(self, name):
        self.__name = name
        
    @staticmethod
    def mymethod(): # no need to pass the self parameter it is a static method not dependent on the class itself
        print('This is a static method')
    
    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}, Gender: {self.__gender}'
        
P1 = Person('John', 25, 'Male')
P1.__name = 'Jane'  # This will not change the name attribute of the object
                    # because __name is a private attribute
                    # This will not change the mangled attribute _Person__name
                    
print(P1.__name)    # This will print 'Jane' because it accesses the new attribute __name

# In summary, P1.__name = 'Jane' creates a new attribute __name in the instance's dictionary, 
# while print(P1.__name) accesses this new attribute. 
# The original mangled attribute _Person__name remains unchanged.

print(P1) # This will print 'Name: John, Age: 25, Gender: Male

P1.Name = 'Boby' # This will change the name attribute of the object
                 # because Name is a property with a setter method
                 
print(P1)        # This will print 'Name: Boby, Age: 25,

Person.mymethod() # This will print 'This is a static method' because it is a static method


        
        