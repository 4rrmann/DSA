class Vehicle:
    def general_usage(self):
        print("general use: Transportation")

class Car(Vehicle): #inherit
    def __init__(self):
        print("suiii Car")
        self.wheel = 4
        self.roof = True

    def specific_usage(self):
        self.general_usage() #from inherit Vehical class
        print("specific use: Squad")

class MotorBike(Vehicle): #inherit
    def __init__(self):
        print("vroom MotorBike")
        self.wheel = 2
        self.roof = False

    def specific_usage(self):
        self.general_usage() #from inherit Vehical class
        print("specific use: Solo/Duo")



c = Car()
c.specific_usage()
print(f"wheel: {c.wheel}, having roof: {c.roof}\n")

print("*"*33, "\n")

c = MotorBike()
c.specific_usage()
print(f"wheel: {c.wheel}, having roof: {c.roof}\n")

print("*"*33, "\n")

print(isinstance(c, Car))
print(isinstance(c, MotorBike), "\n")

print("*"*33, "\n")

print(issubclass(Car, Vehicle)) #Car is a Subclass of Vehicle or not?
print(issubclass(Vehicle, Car))   

print(issubclass(Car, MotorBike), "\n")