""" 
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last == self.n:
            raise StopIteration()
        
        rv = self.last ** 2
        self.last += 1
        return rv
    
g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
    
 """
 
def gen(n):
    for i in range(n):
        yield i ** 2
        
g = gen(10)

print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for i in g:
    print(i)
    

def test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
g = test()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # StopIteration

print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 2
        
values = infinite_sequence()

print(next(values))  
print(next(values))  
print(next(values))  
print(next(values))  
print(next(values))  
print(next(values))  
print(next(values))  
        