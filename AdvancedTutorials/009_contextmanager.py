
file = open('test.txt', 'w')

try:
    file.write("Test")
finally:
    file.close()

# The above code is equivalent to the following code:
with open('test.txt', 'w') as file:
    file.write("hello world")
    
    
    
class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)
        
    def __enter__(self):
        print("Enter")
        return self.file
    
    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        return True
        
        
with File('file.txt', 'w') as file:
    file.write("hello world")
    raise Exception()




from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    file.close()
    print('exit')
    
with file("text.txt", "w") as f:
    f.write("hello world")