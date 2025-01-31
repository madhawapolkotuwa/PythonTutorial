
import inspect

def make_calss(x):
    class Dog:
        def __init__(self, name):
            self.name = name
        def print_value(self):
            print(x)
    return Dog


cls = make_calss(10)
print(cls)

dog = cls("Time")
dog.print_value()

print("----------------------------------------")
print("----------------------------------------")

def func(x):
    if x == 1:
        def rv():
            print("X is equal to 1")
    else:
        def rv():
            print("X is not 1")
    
    return rv

new_func = func(21)
new_func()

print(id(new_func))
print(inspect.getsource(new_func))

# everything happening in Python happens in a live 
# all of the defines, Defines in the memory 