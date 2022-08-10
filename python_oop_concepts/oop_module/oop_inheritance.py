# here "vehicle" class is defined
class vehicle:
    color = "white"
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self,capacity):
        print(f"seating capacity of {self.name} is: {capacity} passengers")
        
    
    def details(self):
        print(f"speed of {self.name} is: {self.max_speed} and mileage is: {self.mileage}")


car = vehicle("Breeza", 80, 30)
car.details()

bus = vehicle("Volvo", 100, 40)
bus.details()  
bus.seating_capacity(60)
print("color is:" + bus.color)          
    
scooty = vehicle("Activa", 60, 20)
scooty.details() 

#print which type of classes objects belongs to
print(type (bus))
print (type(scooty))
print(type(car))
   

# concept of Inheritance
# Here "bikes" class is defined which is derived from "vehicle" class 
class bikes(vehicle):
    pass

tvs = bikes("TVS Apache", 130, 50)
tvs.details()

#print type of tvs
print (type(tvs))

#determine instance using "isinstance"
print(isinstance(tvs, bikes))      # True
print(isinstance(tvs, vehicle))    # True
print(isinstance(car, bikes))      # False