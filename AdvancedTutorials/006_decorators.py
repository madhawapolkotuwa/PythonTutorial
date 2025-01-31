def func(string):
    def wrapper():
        print("started")
        print(string)
        print("Ended")
    
    return wrapper


x = func("hello")
print(x)
x()

print('---------------------------------------')

def SetFunc(f):
    def wrapper():
        print("Set Start")
        f()
        print("Set End")

    return wrapper

def test1():
    print("this is test1")
    
def test2():
    print("this is test2")

fn1 = SetFunc(test1)
print(fn1)
fn1()

fn2 = SetFunc(test2)
print(fn2)
fn2()

print("--------------------------------------")

test1 = SetFunc(test1) # test1 now becomes variable (exact this doing in function decorator)
test2 = SetFunc(test2)

test1()
test2()

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

@SetFunc # need to have wrapper function to call or (implemet and return)
def Run():
    print("this is run")
    
@SetFunc
def Gold():
    print("this is Gold")

Run()
Gold()


print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

# what happens when the functions accepts the arguments
# so we need to tell wrapper to accept any arguments or keywords.
# for work all the function

def SetFunction(f):
    
    def wrapper(*args, **kwords): # accept any arguments or keywords
        print("Start")
        rv = f(*args, **kwords)
        print("End")
        
        return rv
    
    return wrapper

@SetFunction
def a(x):
    print(f"this is a {x}")

@SetFunction
def b(x, y):
    print(f"this is b with {x} : {y}")
    return y
    
a(12)
B = b(24, 5)
print(B)