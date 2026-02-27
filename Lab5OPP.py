from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass

class UberX(Vehicle):

    def calculate_fare(self, distance):
        return distance * 10 
    
    def get_vehicle_type(self):
        return "UberX"

uberx = UberX()
print(uberx.calculate_fare(5))

# Question 1 

# Because Vehicle is an abstract base class 
# (ABC) that contains abstract methods. ABCs are meant 
# to define interfaces, not to be instantiated directly.

# Question 2

# Python will raise a TypeError at runtime when trying 
# to instantiate UberX, because it has not implemented 
# all abstract methods from Vehicle.

# Question 3

# At runtime. Python checks for unimplemented abstract
# methods only when the object is instantiated, not during 
# class definition.

# Question 4

# It ensures consistency across all vehicle types. Every 
# vehicle must implement the required methods, making the 
# system reliable and easier to extend.

class UberBike(Vehicle):

    def calculate_fare(self, distance):
        return distance * 5 
    
    def get_vehicle_type(self):
        return "UberBike"
    
uberx = UberX() 
bike = UberBike()

print(isinstance(uberx, Vehicle))
print(isinstance(bike, Vehicle))

# Question 1 

# Yes, because it inherits from Vehicle, so it is
# considered a subtype of Vehicle.

# Question 2

# It becomes a standalone class and is no longer considered a 
# Vehicle. It won't be part of the vehicle group and may 
# not work in polymorphic contexts.

# Question 3 

# IS-A. UberBike is a Vehicle.

vehicles = [UberX(), UberBike()]

for vehicle in vehicles:
    print(vehicle.get_vehicle_type(),
          vehicle.calculate_fare(10))
    
# Question 1 

# In the loop when calculate_fare() and get_vehicle_type() 
# are called on each object. The correct method is chosen
# dynamically based on the object's actual class.

# Question 2

# Polymorphism would break because the loop expects the same 
# method names. You'd need conditional logic to handle different 
# types.

# Question 3 

# It’s more scalable and maintainable. New vehicle types can be 
# added without modifying existing code that uses them.

class ElectricMixin:
    
    def charge_battery(self):
        return "Charging batery...."
    
class UberGreen(ElectricMixin, UberX):
    pass

green = UberGreen()

print(green.get_vehicle_type())
print(green.charge_battery())

# Question 1 

# It doesn't have to be, but in some languages 
# method resolution order (MRO) gives priority to the 
# first class. If both classes define the same method, 
# the first one wins.

# Question 2 

# No, it’s modeling HAS-A behavior. It adds functionality 
# (charging) without implying a strict “is-a” relationship.

# Question 3 

# Python uses the Method Resolution Order (MRO) 
# to decide which method to call. The first class in 
# the inheritance chain that defines the method will be used.

class Driver:

    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def start_trip(self, distance):
        fare = self.vehicle.calculate_fare(distance)
        return f"{self.name} driving {self.vehicle.get_vehicle_type()} - Fare: {fare}"
    

driver1 = Driver("Alice", UberX())
driver2 = Driver("Bob", UberBike())

print(driver1.start_trip(10))
print(driver2.start_trip(10))

# Question 1 

# No, Driver contains a Vehicle object but does 
# not inherit from it.

# Question 2

# Composition (HAS-A). A driver has a vehicle.

# Question 3 

# Because you can change the vehicle at runtime 
# or assign different vehicle types to a driver 
# without changing the Driver class.

class UberApp:

    def request_ride(self, driver, distance): 
        return driver.start_trip(distance)
    
app = UberApp()

print(app.request_ride(driver1, 5))

# Question 1 

# Dependency is temporary; composition is permanent.

# Question 2

# No. It only uses a Driver instance while processing
#  the request_ride method. Once the method ends, the
#  reference can be discarded.

# Question 3

# Loose coupling means classes rely on interfaces or temporary usage, not concrete implementations.
# Benefits:
# Easier to modify one class without affecting others.
# Supports testing and mocking.
# Facilitates adding new features (like new vehicle types)
#  without rewriting UberApp.


# FINAL QUESTIONS 

# Question 1 

# UberX IS-A Vehicle
# UberBike IS-A Vehicle
# UberGreen IS-A UberX
# UberGreen IS-A Vehicle (indirectly through UberX)

# Question 2 

# Driver HAS-A Vehicle

# Question 3

# UberApp USES-A Driver

# Question 4

# Runtime polymorphism happens when the same 
# method call behaves differently depending 
# on the object type.

# Question 5

# TThis design supports adding new vehicle 
# types because the abstract class Vehicle 
# defines a common structure that all vehicles 
# must follow. Any new vehicle class only needs 
# to inherit from Vehicle and implement the required 
# methods calculate_fare() and get_vehicle_type(). Once 
# the new class is created, it will automatically work 
# with the Driver class, the UberApp class, and any loops 
# that process Vehicle objects. This makes the system easy 
# to extend without changing existing code, which improves 
# maintainability and scalability.
