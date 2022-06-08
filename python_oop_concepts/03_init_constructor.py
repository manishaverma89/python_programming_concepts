class Employee:
    def __init__(self, emp_name, emp_age, emp_salary):  # self can be any variable name, doesn't have to be named self
        self.name = emp_name
        self.age = emp_age
        self.salary = emp_salary
    def message(self):
        print(f"Hello employee's information is: , {self.__dict__}")    
    

emp1 = Employee("Manisha", 32, 800)
emp2 = Employee("Atharv", 3, 600)
# print(emp1.__dict__)
# print(emp2.__dict__)

emp1.message()




