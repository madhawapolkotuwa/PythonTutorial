# video :-
# https://youtu.be/NAQEj-c2CI8?list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP
#
#

print(type(2)) # <class 'int'>
print('--------------------------------------')
print(type(2.2)) # <class 'float'>
print('--------------------------------------')
print(type("sfjsld")) # <class 'float'>
print('--------------------------------------')

def func():
    pass
print(type(func)) # <class 'function'>
print('--------------------------------------')

class Test:
    pass

print(type(Test)) # <class 'type'>

print('--------------------------------------')

Test2 = type('Test2', () , {} ) # this is completly equal to class Test2: pass

print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')

class Foo:
    def show(self):
        print("hi")
        
def add_attribute(self):
    self.z = 9
    

TestCls = type('TestCls', (Foo,), { "x":5 , "add_attribute":add_attribute})
t = TestCls()
print(t.x)
t.xy = "Hello" # this way we cant define attribute outside the class
print(t.xy)

t.show()

t.add_attribute()
print(t.z)



print('--------------------------------------')
print('-----------meta class-----------------')
print('--------------------------------------\n')


class Meta(type):
    def __new__(self, class_name, bases, attrs): # all befor the call __init__
        print(attrs)
        
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
                
        print(a)
        return type(class_name, bases, a)
    
class Dog(metaclass=Meta):
    x = 5
    y = 8
    
    def name(self):
        print("Tim")

d = Dog()

d.NAME()
