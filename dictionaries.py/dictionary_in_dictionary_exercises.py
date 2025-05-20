ricky = {'firstname': 'riccardo',
'surname': "d'alleva",
'age': 31,
'city': 'stuttgart',
}

hope = {
    'firstname': 'hope',
    'surname': 'kombo',
    'age': 23,
    'city': 'wolverhampton',       
}

yunjin = {
    'firstname': 'jennifer',
    'surname': 'huh',
    'age': 23,
    'city': 'seoul',
}

people = [ricky, hope, yunjin]

for  user_info in people:
    print("\n" + user_info['firstname'].title() + " " + user_info['surname'].title())
    print(user_info['age'])
    print(user_info['city'].title())


##########

sky = {
    'name': 'sky',
    'kind': 'cat',
    'owner': ['hope', 'bless', 'celeste', 'welcome']
}

bella = {
    'name': 'bella',
    'kind': 'dog',
    'owner': 'john'
}

sybil = {
    'name': 'sybil',
    'kind': 'hamster',
    'owner': 'karina'
}

heather = {
    'name': 'heather',
    'kind': 'snake',
    'owner': 'tyler'
}

donald = {
    'name': 'donald',
    'kind': 'duck',
    'owner': 'walt'
}

mickey = {
    'name': 'mickey',
    'kind': 'mouse',
    'owner': 'walt'

}

minnie = {
    'name': 'minnie',
    'kind': 'mouse',
    'owner': 'walt'
}

dumbo = {
    'name': 'dumbo',
    'kind': 'elephant',
    'owner': 'walt'

}

winnie = {
    'name': 'winnie',
    'kind': 'bear',
    'owner': 'walt'
}

pets = [sky, bella, sybil, heather, donald, mickey, minnie, dumbo, winnie]

for pet in pets:
    if len(pet['owner']) > 1:
        print("\n" + pet['name'].title() + ", " + pet['kind'].title() + ", " + str(pet['owner']).title())
    else:
        print("\n" + pet['name'].title() + ", " + pet['kind'].title() + ", " + pet['owner'].title())

#############

favourite_places = {
    'hope': ['paris', 'disneyland paris', 'rome'],
    'ricky': ['orsogna', 'francavilla'],
    'bill gates': ['johannesburg', 'cairo', 'nairobi']
}

for name, places in favourite_places.items():
    print(name.title() + "'s favourite places to visit are: " + ', '  .join(places).title() + ".")
# .join() joins elements of a sequence like a list into a single string

#############

favourite_number = {'bless': [22, 42],
'celeste': [44, 16],
'welcome': [26, 30, 77, 60],
'riccardo': [25, 93],
'hamdiya': [17, 1, 100]    
}

for name, numbers in favourite_number.items():
    print(name.title() + "'s favourite number's are: " + ', ' .join(str(num) for num in numbers) + '.')
# str(num) for num in numbers is a generator expression that converts each number in the list to a string.
 # ', '.join() joins each stringified number with a comma and a space.

##############

cities = {
    'new york': {
        'country': 'america',
        'population': 8258000,
        'fact': 'most populous city in the us',
 
    },

'paris': {
    'country': 'france',
    'population': 2103000,
    'fact': 'paris was once roman'
    },

    'rome': {
        'country': 'italy',
        'population': 2760000,
        'fact': 'more fountains than any other city in the world'
    }
}

for city, city_info in cities.items():
    print('\n' + city.title())
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("Located in " + country.title() + ", with a population of " + 
          str(population) + ", \nRandom fact: " + fact.title())
    
    