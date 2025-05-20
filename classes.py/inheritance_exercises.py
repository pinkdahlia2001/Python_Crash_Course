# ICE CREAM STAND #
"""A set of classes that can be used to represent restaurants."""
class Restaurant():
    """Prints simple information about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # this is an attribute.

    def describe_restaurant(self):
        """Prints the name and cuisine of the restaurant."""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Prints that the cuisine is open."""
        print(self.restaurant_name.title() + " is open.")

    def read_number_served(self):
        """Reads the number of customers served."""
        print(self.restaurant_name.title() + " has served " +
               str(self.number_served) + " customers.")
        
    def set_number_served(self, customers):
        """Allows user to manually update number served."""
        self.number_served = customers

    def increment_number_served(self, customer_no):
        """Adds the given amount to amount of customers served."""
        self.number_served += customer_no

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise the attributes of the parent class and the flavours."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'cookie dough', 'baileys', 'salted caramel']

    def get_flavours(self):
        """Prints a simple message about ice cream flavours on offer."""
        print("These are our currently available ice cream flavours: " + (', '.join(self.flavours)) + ".")
        
    
eis = IceCreamStand ('ice stone', 'gelateria')
eis.get_flavours()


########

class User():
    """Collects user info."""
    def __init__(self, first_name, last_name, city, country, age = "", sex = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.country = country
        self.age = age
        self.sex = sex
        self.login_attempt_count = 0

    def describe_user(self):
        """Prints collected user info."""
        print("\nName: " + self.first_name.title() + " " + self.last_name.title())
        print("Location: " + self.city.title() + ", " + self.country.title())
        
        if self.age != "":
            print("Age: " + str(self.age))
        else:
            print("Age: Unknown")

        if self.sex != "":
            print("Sex: " + self.sex.title())
        else:
            print("Sex: Unknown")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + " " + self.last_name.title() + "!")


    def show_login_attempts(self):
        print("You have attempted to log in " + str(self.login_attempt_count) + " times.")

    def increment_login_attempts(self, attempt_num = 1):
        self.login_attempt_count += attempt_num  

    def reset_login_attempts(self):
            self.login_attempt_count = 0

class Privileges():

    def __init__(self, privileges=None):
        """Initialise the privileges attributes."""
        
        if privileges is None:
            privileges = ['can add post', 'can delete post', 
                           'can ban user', 'can modify content']
        self.privileges = privileges
    
        
        
    def show_privileges(self):
        """Prints a simple list of admin privileges."""
        print("Admins have the following privileges: " + (', '.join(self.privileges)) + ".")


class Admin(User):

    def __init__(self, first_name, last_name, city, country, age="", sex=""):
        """Initialise the attributes of the parent class and the flavours."""
        super().__init__(first_name, last_name, city, country, age, sex)
       
       
        self.privileges = Privileges()

user_admin = Admin("john", "doe", "paris", "france")
user_admin.privileges.show_privileges()

####

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

    def upgrade_battery(self, battery_size=85):
        """Increases the battery size."""
        self.battery_size = battery_size



        
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

electric_cleo = ElectricCar('Renault', 'Clio E-Tech', '2024')
electric_cleo.battery.get_range()
electric_cleo.battery.upgrade_battery()
electric_cleo.battery.get_range()

