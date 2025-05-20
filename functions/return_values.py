# Returning a simple value #

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name 
    return full_name.title() # returns the result of the function back to the caller.
# the function sends the formatted full_name back to the line where the function was called.
# return allows the result of the function to be used elsewhere in the program.
# a variable needs to be provided to store the return value, which in this case is musician.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an argument optional #

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('onika', 'tanya', 'maraj')
print(musician)

# middle names aren't always necessary, and this function wouldn't work if you tried to call it with only a first and last name.
# can combat this by giving middle name a default value of an empty string.

def get_formatted_name(first_name, last_name, middle_name=''): # first name and last name are required parameters, while middle name is optional.
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('onika', 'maraj', 'tanya')
print(musician)

# the '' in middle_name means that if a caller does not provide a middle name, it will be empty by default.
# because it is optional, middle name is defined, last.

# you can use keyword argument if you want to put middle name in the middle
musician = get_formatted_name(first_name='onika', middle_name ='tanya', last_name='maraj')

# RETURNING A DICTIONARY #

# functions can return any kind of vlaues, including lists and dictionaries.

def build_person(first_name, last_name, age=""):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('billie', 'eilish', age = 23)
print(musician)

# Using a function with a while loop #

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


#### exercises ####

def city_country(city, country):
    """Returns a print of city and country, neatly formatted."""
    stadt_land = '"'+ city + ", " + country + '"'
    return stadt_land.title()

rome = city_country('rome', 'paris')
print(rome)

paris = city_country(country = "france", city = 'paris')
print(paris)

australia = city_country(city='sydney', country='australia')
print(australia)

#

def make_album(name, title, track_count=""):
    album = {'artist': name, 'album_title': title}
    if track_count:
        album['track_count'] = track_count
    return album


sza = make_album('SZA', 'ctrl')
print(sza)

aespa = make_album('Aespa', 'Armageddon')
print(aespa)

temmis = make_album("TEMMIS", 'TREPPENHAUS')
print(temmis)

charli_xcx = make_album("charli xcx", "BRAT", 15)
print(charli_xcx)

#

import printing_functions

amy = printing_functions.make_album('amy winehouse', 'back to black', 2)
print(amy)

from printing_functions import make_album