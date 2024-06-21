# Overriding
class A:
    classVar1 = "Class variable in class A"

    def __init__(self):
        self.var1 = "Variable inside class A"
        self.classVar1 = "Instance var in class A"
        self.special = "special"

class B(A):
    classVar1 = "Class variable in class B"

    def __init__(self):
        self.var1 = "Variable inside class B"
        self.classVar1 = "Instance var in class B"
    
a = A()
b = B()

print(a.classVar1)
print(b.classVar1)
#print(b.special) # wont work, super() needs to be used

# if we override the constructor in the child class, then for the instance of the child class, the parent class's __init__ is gone
# But if we still want to use the "special" of class A __init__ after overriding the __init__ in class B we need to use the super() fucntion
class C(A):
    classVar1 = "Class variable in class C"

    def __init__(self):
        super().__init__()
        self.var1 = "Variable inside class C"
        self.classVar1 = "Instance var in class C"
    
c = C()
print(c.special)

# super - is used to access the class methods (constructors ...) from the parent class