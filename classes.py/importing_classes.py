# You can store classes in modules and then import the classes needed into the main program.

from car import Car
from electric_car import ElectricCar

my_new_car = Car('renault', 'clio', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from car import Car, ElectricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_fiat = ElectricCar('fiat', '500E', 2024)
print(my_fiat.get_descriptive_name())


import car # importing the whole module, including ElectricCar class child.

my_beetle = car.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_fiat = car.ElectricCar('fiat', '500E', 2024)
print(my_fiat.get_descriptive_name())


                