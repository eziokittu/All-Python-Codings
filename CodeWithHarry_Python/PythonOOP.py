# Defining a class
class Employee:
    # class member variables
    no_of_leaves = 8

    # defining a member function of the class
    def PrintDetails(self):
        print(f"Name is {self.name}. Roll is {self.roll} and Maths marks is {self.marks}")

    # defining a constructor
    # NOTE : without this constructor, always a default constructor is created
    def __init__(self, aname, aroll, amarks):
        self.name = aname
        self.roll = aroll
        self.marks = amarks
    
    # using decorators
    @classmethod # those methods that are only for pure class methods and not for instances
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves
    
    # way to create alternative constructor using the decorator whic takes a string
    @classmethod
    def from_str(cls, string):
        #params = string.split("-")
        #return cls(params[0], params[1], params[2])
        return cls(*string.split("-")) # in 1 line for the above 2 lines

    @staticmethod # those methods which are neither class nor instance related
    def PrintGood(name):
        print(f"{name} is a good person")

# harry is an instance of the class
harry = Employee("Harry", 2, 97)

# instance vaariables
# harry.name = "Harry"
# harry.roll = 2
# harry.marks = 89
harry.no_of_leaves = 18

# calling the member function through the instance
harry.PrintDetails()

# printing the instance variable
print(harry.no_of_leaves)
# printing the class member variabe
print(Employee.no_of_leaves)
#NOTE : if there was no instance variable "no_of_leaves" in the instance then it would refer to the class member variable

# the class method will have no effect when called from an instance, but the class member variable will change
harry.change_leaves(83)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)

# using the alternative constructor, where arguement is passed in the form of a 1 line string
karan = Employee.from_str("Karan Chopra-4-78")
karan.PrintDetails()
karan.PrintGood(karan.name)


# INHERITANCE

# Single level Inheritance - class Programmer is inheriting from class Employee
class Programmer(Employee):
    # without using super()
    def __init__(self, aname, aroll, amarks, alanguages):
        self.name = aname
        self.roll = aroll
        self.marks = amarks
        self.languages = alanguages

    def PrintDetails_Prog(self):
        print(f"Name is {self.name}. Roll is {self.roll} and Maths marks is {self.marks}. Languages are {self.languages}")

# inheriting all the methods of parent class
#subham = Programmer.from_str("Subham Bose-14-99") # after changing the __init__ this wont work
#subham.PrintDetails()

# calling the constructor of newly created __init__
mohan = Programmer("Mohan Kumar", 7, 66, ["C++", "Objective-C", "Java", "Python"])
mohan.PrintDetails_Prog()


# Multiple Inheritance
class Player:
    var1 = 10 #public variable
    _var2 = 100 #protected variable
    __var3 = 1000 #private variable


    no_of_games = 4
    def __init__(self, aname, agame):
        self.name = aname
        self.game = agame

    def PrintDetails_Player(self):
        print(f"Name is {self.name}. Game is {self.game}")

rohan = Player("Rohan Das", ["Cricket", "Football", "Tennis"])
print(rohan.var1)
print(rohan._var2)
print(rohan._Player__var3) # name handling used to access the private data of the class, otherwise this data cannot be accessed

# CoolEmployee class is inheriting both the classes , the order is important
class CoolEmployee(Employee, Player):
    pass

mayank = CoolEmployee("Mayank Malhotra", 17, 75)
mayank.PrintDetails()