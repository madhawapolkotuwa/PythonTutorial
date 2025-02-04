from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractmethod
    def person_method():
        """ Interface Method """
        
class Student(IPerson):
    
    def __init__(self):
        self.name = "Default student name"
        
    def person_method(self):
        print("I am a Student")
        
class Teacher(IPerson):
    
    def __init__(self):
        self.name = "Default teacher name"
        
    def person_method(self):
        print("I am a Teacher")
        
        
class PersonFactory: # dynamic object creation
    
    @staticmethod
    def create_person(person_type):
        if person_type == 'Student':
            return Student()
        elif person_type == 'Teacher':
            return Teacher()
        # raise an error if the person_type is not 'Student' or 'Teacher'
        
#p1 = IPerson() # This will raise an error because IPerson is an abstract class
               # Can't instantiate abstract class IPerson with abstract method person_method

s1 = Student()
s1.person_method() # This will print 'I am a Student'
 
t1 = Teacher()
t1.person_method() # This will print 'I am a Teacher'

if __name__ == "__main__":
    choice = input("Enter your choice (Student/Teacher): ")
    PersonFactory.create_person(choice).person_method()




               


               
               
        