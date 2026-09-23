# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def drive(self, speed):
            self.mode = "driving"
            self.speed = speed

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} with {self.doors} doors")

    def drive(self, speed):
        super().drive(speed)
        print(f"The car is now driving at {self.speed} mph.")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} ({self.type})")

    def drive(self, speed):
        super().drive(speed)
        print(f"The motorcycle is now driving at {self.speed} mph.")
# Example usage
my_car = Car("Toyota", "Corolla", 2020, 4)
my_car.display_info()
print(my_car.doors)
my_car.drive(60)

my_truck = Vehicle("Ford", "F-150", 2018)
my_truck.display_info()

my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, "cruiser")
my_motorcycle.display_info()
my_motorcycle.drive(50)

my_bike = Vehicle("Trek", "Marlin 7", 2022)
my_bike.display_info()