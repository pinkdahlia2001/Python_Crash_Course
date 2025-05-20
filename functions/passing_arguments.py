# positional arguments #

def describe_pet(animal_type, pet_name): # When the function is called, arguments are passed in a specific order, and their position determines which parameter each value is assigned to.
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("cat", "sky")
describe_pet("cat", "cloud")
describe_pet("cat", "astro")
describe_pet("cat", "moonlight")
# Arguments are in the same order as the parameters in the function.
# order matters. the arguments need to be in the same order as the parameters.

# KEY ARGUMENTS #

# a keyword argument is a name-value pair that you pass to a function.
# you directly associate the name and value within the argument, so when you pass the argument to the function, there's no confusion.

describe_pet(animal_type='cat', pet_name='sky')
describe_pet(pet_name='astro', animal_type='cat')

# DEFAULT VALUES #

# when you define a default value for a parameter, you can exclude the corresponding argument you'd usually write in the function call.
# using default values simplifies function calls and clarifies the ways in which functions are typically used.

def describe_pet(pet_name, animal_type='cat'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='sky')

# now when no animal type is specified, the default is cat.
# python still interprets this as a positional argument, so if the function is called w/ just pet's name, that argument will match up with the first parameter listed in the function's definition.
# that's why the first parameter needs to be pet_name.
describe_pet('astro')

describe_pet(pet_name='blob', animal_type='goldfish')
# to describe an animal other than a cat, use a function call like the above.
# because an explicit argument for animal_type is provided, the default value of the parameter will be ignored.

# EQUIVALENT FUNCTION CALLS #

# positional arguments, keyword arguments, and default values can all be used together, so there are many different ways to write the same function.

########

def make_shirt(size = 'Large', message = 'I love Python.'):
    """Prints the size of a shirt and the message to be printed on it."""
    print("Size: " + size + "\nMessage: " + message)

make_shirt(size = 'XXS' , message = "hope rocks")
make_shirt('XXS', 'i <3 hope')
make_shirt()
make_shirt('medium')

######

def describe_city(city, country = 'England'):
    """Prints a simple description of a city"""
    print(city.title() + " is in " + country.title() +)

describe_city('wolverhampton')
describe_city(city='bristol')
describe_city('paris', 'france')