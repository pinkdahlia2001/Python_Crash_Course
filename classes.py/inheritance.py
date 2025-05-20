# If the class you're writing is a specialised version of another class you've written, you can use inheritance.
# When one class inherits another, it automatically takes on all the attributes and methods of the first class.
# original class = parent class
# new class = child class = inherits every attribute and method, but is also free to define new attributes and methods of its own.

# the __init__() method for a child class #

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery(): # Can create new classes when one class has too many attributes and methods.
    # This class doesn't inherit from any class, like ElectricCar does.
    """A simple attempt to model a battery for an electric car."""

    def __init__ (self, battery_size=70):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240

        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full range."
        print(message)
        
# When creating a child class, the parent class must be part of the current file and appear before the child class.
class ElectricCar(Car): # The name of parent class should also be included in the parenthesis.
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # init takes in info required to make the Car instance. super() function helps Python make connection between parent and child class.
        """
        Initialise attributes of the parent class.
        Then initialises attributes specific to an electric car.
        """

        super().__init__(make, model, year) # These attributes are only associated with all instances created from the electric car class.
        self.battery = Battery()


    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_fiat = ElectricCar('fiat', '500E', '2024')
print(my_fiat.get_descriptive_name()) 
my_fiat.battery.describe_battery() # tells Python to look at the instance my_fiat, find its battery attribute, and then call the method describe_battery that's associated with the Battery instance stored in the attribute.
my_fiat.battery.get_range()

