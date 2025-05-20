def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'pepperoni', 'extra cheese')
# the asterik (*) in the parameter name *toppings creates an empty tuple called toppings and puts whatever values it receives into the typle.
# even if the function only receives one value, it is still packed into a typle.

def make_pizza(*toppings):
    """Summarise the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings: print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'pepperoni', 'extra cheese')

# USING ARBITRARY KEYWORD ARGUMENTS #

# When you don't know ahead of time what kind of info will be passed to the function, you can write functions that accept as many key-value pairs as the statement provides.
# e.g. building user profiles, you know you'll get info abut a user, but dont know what KIND of info you'll receive.
# the build_profile def always takes a first and last name, but accepts an arbitrary number of keyword arguments too.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {} # this dictionary holds the user's profile.
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): # loop through the additional key-value pairs in the dictionary user_info and add each pair to the profile dictionary.
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# the double asteriks (**) in **user_info cause Python to create an empty dictionary called user_info and puts the key value pairs it receives into this dictionary.
# within the function, you can access the name-value pairs in user_info like any normal dictionary.

### EXERCISES ###


def make_sandwich(*sandwich_fillings):
    """Prints out sandwich fillings."""
    for filling in sandwich_fillings:
        print(filling.capitalize() + " has been added." )
    print("Your sandwich has finished being prepared.")

make_sandwich('turkey ham', 'cheddar cheese', 'lettuce', 'tomatoes', 'mayonnaise')


#
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {} # this dictionary holds the user's profile.
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): # loop through the additional key-value pairs in the dictionary user_info and add each pair to the profile dictionary.
        profile[key] = value
    return profile

user_profile = build_profile('hope', 'kombo', 
              age = 23, 
              ethnicity = 'congolese', 
              favourite_colour= 'pink')

print(user_profile)

#

def make_car(manufacturer, model, **car_info):
    """Builds a dictionary containing information about cars"""
    car_profile = {}
    car_profile['car_manufacturer'] = manufacturer
    car_profile['car_model'] = model
    for k, v in car_info.items():
        car_profile[k] = v
    return car_profile

car_information = make_car('fiat', 500,
                           colour = 'red',
                           year = 2024)

print(car_information)