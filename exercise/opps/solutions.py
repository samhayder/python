class Car():
    car_count = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        self.car_count += 1
        
    #5-Polymorphism
    def fuel_type(self):
        return "Diesel or petrol"
        
    #2-Add a method
    def full_name(self):
        return f"Brand- {self.__brand}, Model- {self.__model}, Fuel Type-{self.fuel_type()}"
    
    #4-Private to access get method
    def get_brand(self):
        return self.__brand
    
    #7-Static method
    @staticmethod
    def general_description():
        return "This is the general description on the car."
    
    #8-property decorator
    @property
    def model(self):
        return self.__model

#3-Inheritance
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    #5-Polymorphism
    def fuel_type(self):
        return "Electric Charge"
        
    def full_name(self):
        return super().full_name() + f", Battery Size- {self.battery_size}"


toyota = Car("Toyota", "X-Korolla")
print(toyota.full_name())
tesla = ElectricCar("Tesla", "s", "15kWh")
print(tesla.full_name())
print(tesla.get_brand())
print(Car.general_description())
# tesla.model = "Nicola"
print(tesla.model)

#10-Multiple Inheritance
class Battery:
    def batter_info(self):
        return "Battery info..."

class Engine:
    def engine_info(self):
        return "Engine info..."

class Electric(Battery,Engine,ElectricCar):
    pass
    
electric_one = Electric("Benz","xy2z","0.25hp")
print(electric_one.batter_info())
print(electric_one.engine_info())