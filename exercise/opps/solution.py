class Car():
  car_count = 0 #6-Class Variable
  
  def __init__(self,brand,model):
    self.__brand = brand #4-Encapsulation
    self.model = model
    Car.car_count += 1
  
  def get_brand(self): #4-Encapsulation
    return self.__brand
    
  def fuel_type(self): #5-Polymorphism
    return "Fuel Type- Diesel or Octan"
  
  def full_name(self): #2-class method
    return f"Brand- {self.__brand}, Model- {self.model}, " + self.fuel_type()

    
  

class ElectricCar(Car): #3-Inheritance
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size
    
  def fuel_type(self): #5-Polymorphism
    return "Fuel Type- Electric Charge"

  def full_name(self):
    return super().full_name() + f", Battery Size- {self.battery_size}"#Polymorphism
  
  
tata = Car("Tata", "Indian")
print(tata.full_name())
print(tata.get_brand())
print(tata.model)

tesla = ElectricCar("Tesla", "x", "85kWh")
print(tesla.full_name())

print(tesla.fuel_type())

print(Car.car_count)