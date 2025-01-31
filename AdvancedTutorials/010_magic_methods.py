
print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __del__(self):
        print(f"{self.name} has been deleted")
        
p = Person("John", 30)

del p # if we delete the object, __del__ method will be called
      # if we not delete the object, __del__ method automatically called when program ends
      # __del__ method is called when object is deleted from memory


print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        if isinstance(other, (int,float)):
            return Vector(self.x + other, self.y + other)
        return Vector(self.x + other.x, self.y + other.y)
    
    def __radd__(self,other): # other + self
        return self + other
    
    def __neg__(self): #-self
        return Vector(-self.x, -self.y)

    def __sub__(self,other): # self - other
        return self + (other * -1)
    
    def __rsub__(self,other): # other - self
        return self - other
    
    def __mul__(self,other): # self * other
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int,float)  ):
            return Vector(self.x * other, self.y * other) 
        else:
            raise TypeError("Expected Vector or int or float")
        
    def __rmul__(self,other): # other * self
        return self * other
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __call__(self):
        print(f"Vector({self.x},{self.y})")
    
v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 + v2) # (7, 8)
print(v1 - v2) # (-3, 12)
print(v1 * v2) # -10
print(v1 * 2)  # (4, 20)  
print(2 * v1)  # (4, 20)
print(-v1)     # (-2, -10)
print(1 - v2)  # (4, -3)
print(v2 - 2.5)  # (2.5, -4.5)

value = v1 * v2
#value() #  error because v1 * v2 return int not Vector object
v3 = v1 + v2
v3() # Vector(7,8) because __call__ method is called
