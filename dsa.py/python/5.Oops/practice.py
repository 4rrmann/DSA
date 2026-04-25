class Car:
    total_car = 0 #Class variable

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    def full_name(self): #Class Methos & Self
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self): #Encapsulation
        return self.__brand + " !"
    
    def fuel_type(self): #Polymorphism
        return "Petrol & Diseal"
    
    @staticmethod #Decorators
    def general_description():
        return "Cars are means of transport."
    
    @property #Decorators
    def model(self):
        return self.__model

    
class ElectricCar(Car): #Inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): #Polymorphism
        return "Electric charge"


my_car = Car("Toyota", "Corolla")
# my_car.model = "City"
# print(f"Brand: {my_car.brand} \nModel: {my_car.model}")

print(f"Model: {my_car.model}") #without `@property` it gives "City" but with `@property` it throws an error

# print(f"\n fullname: {my_car.full_name()}")

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla, ElectricCar))

# print(f"\n{my_tesla.full_name()}")
# print(my_tesla.battery_size)
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

print(Car.total_car)
# print(my_car.get_brand())

print(f"\n{Car.general_description()}\n")


#Multiple Inheritance
class Battery:
    def battery_info(self):
        return "this is Battery"

class Engine:
    def engine_info(self):
        return "this is Engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())