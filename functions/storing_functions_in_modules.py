# You can store functions in a separate file called a module and then importing that module into your main program.
# An import statement tells Python to make the code in a module available in the currently running program file.
# Storing functions in a separate file allows you to hide the details of your programs code and focus on its higher-level logic.

# A module is a file ending in .py that contains the code you want to import into your program.

def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# #This is what the code looks like in the other file:
import storing_functions_in_modules

storing_functions_in_modules.make_pizza(16, 'pepperoni')
storing_functions_in_modules.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import storing_functions_in_modules tells Python to open the file storing_functions_in_modules.py and copy all functions into this program.
# to call a function from an imported module, enter the name of the module that was imported, followed by the name of the function, separated by a dot.
# module_name.function_name() 

# the import statement makes every function from the module available in your program.


## IMPORTING SPECIFIC FUNCTIONS ##

# to import specific functions from a module, use this general syntax:
# from module_name import function_name 

# You can import as many functions as you want, each separated with a comma
# from module_name import function_0, function_1, function_2

# then if you import just specific functions, you use the function "normally"

from storing_functions_in_modules import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# You can also use alias for functions
# from module_name import function_name as fn

from storing_functions_in_modules import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# modules can also be given alias

import storing_functions_in_modules as s
s.make_pizza(16, 'pepperoni')
s.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# you can also import all functions in a module using an asterisk (*)
# best to not use with larger modules you didn't write.
# it's better to specify which functions you use, or import the entire module using the dot notation
from storing_functions_in_modules import *

make_pizza(16, 'pepperoni')

# STYLING FUNCTIONS #

def function_name(parameter_0, parameter_1='default value')
    
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    #function body....


