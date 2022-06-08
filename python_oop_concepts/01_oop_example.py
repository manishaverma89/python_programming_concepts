class Employee:
    head_office = "Ambala"   # class variable
    pass                                                            

manisha = Employee()    # created objects manisha and atharv
atharv = Employee()

manisha.name = "Manisha"
manisha.std = "MCA"
manisha.age = 32
manisha.salary = 800

atharv.name = "Atharv"
atharv.std = 2
atharv.age =3
atharv.salary = 500

print(atharv.name)
print(atharv.age)
print(atharv.__dict__)

print(manisha.name)
print(manisha.age)
print(manisha.__dict__)
print(Employee.__dict__)
manisha.head_office = "Jagadhri"    #instances can't change the class variables, can only be chnaged by class
print(manisha.__dict__)
print(manisha.head_office)