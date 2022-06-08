# Parent class
class Parent:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def print_message(self):
        print(f"Hello, My name is {self.first_name} {self.last_name} ")
        
        
# To keep the inheritance of the Parent's __init__() function, add a call to the Parent's __init__() function 
class Child1(Parent):
    def __init__(self, fname, lname):
        Parent.__init__(self, fname, lname)

        
# Child's __init__() func overrides the properties of the Parent's __init__() function
class Child2(Parent):
    def __init__(self, name ):
        self.fullname = name
    def message(self):
        print(f"Hi my name is {self.fullname}")
        
# use the super() function
# super() function that will make the child class inherit all the methods and properties from its parent:
class Child3(Parent):
    def __init__(self, fname, lname, ch_age):
        self.age = ch_age
        super().__init__(fname, lname)   # self is not written here
    
    def welcome(self):
        print(f"Hii my name is {self.first_name} {self.last_name} , my age is {self.age} ")
                                                                                                              


        
ch1 = Child1("Bhavya", "Verma")                #  object Child1
print(ch1.print_message())        
        
ch2 = Child2("Aarav Verma")                    #  object Child2
print(ch2.message())

ch3 = Child3("Misha", "Verma", 22)             #  object Child3
print(ch3.print_message())
print(ch3.welcome())

p = Parent("Manisha", "Verma")                 #  object Parent
print(p.print_message())


