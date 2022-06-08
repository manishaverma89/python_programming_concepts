class Employee:
    def emp_Details(self):
        return f"{self.name} is very smart employee having age {self.age} and role is {self.role}"
    


manisha = Employee()
atharv = Employee()

manisha.name = "Manisha"
manisha.age = 32
manisha.role = "Developer"

atharv.name = "Atharv"
atharv.role = "Engineer"
atharv.age =3


print(atharv.emp_Details())
print(manisha.emp_Details())