import time

def timer(func):
    
    def wrapper(*args, **kwords):
        start = time.time()
        rv = func(*args,**kwords)
        total = time.time() - start
        print("Time: ", total)
        
        return rv
        
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass

@timer
def test2():
    time.sleep(1.0)
    
test()
test2()