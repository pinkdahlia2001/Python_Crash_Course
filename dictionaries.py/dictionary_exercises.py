boyfriend = {'firstname': 'riccardo',
'surname': "d'alleva",
'age': '31',
'city': 'stuttgart',
}

print(boyfriend['firstname'].title())
print(boyfriend['surname'].title())
print(boyfriend[str('age')])
print(boyfriend['city'].title())

#########

favourite_number = {'bless': 22,
'celeste': 44,
'welcome': 26,
'riccardo': 25,
'hamdiya': 17,    
}

print("Bless's favourite number is " + str(favourite_number['bless']) + ".")

print("Celeste's favourite number is " + str(favourite_number['celeste']) + ".")
      
print("Welcome's favourite number is " + str(favourite_number['welcome'])+ ".")

print("Riccardo's favourite number is " + str(favourite_number['riccardo']) + '.')

print("Hamdiya's favourite number is " + str(favourite_number['hamdiya'])+ ".")

##############

glossary = {}

glossary['variable'] = "a value stored in memory"
glossary['function'] = "a block of reusable code that performs a specific task"
glossary['list'] = "an ordered collection of items"
glossary['dictionary'] = 'an unordered collection of key-value pairs'
glossary['loop'] = 'allows for repeated execution of a block of code'

print(glossary)

print("\nVariable - " + glossary['variable'] + ".")
print("\nFunction - " + glossary['function'] + ".")
print("\nList - " + glossary['list'] + ".")
print("\nDictionary - " + glossary['list'] + ".")
print("\nLoop - "+ glossary['loop'] + ".")

for term, definition in glossary.items():
    print("\n" + term.title() + " - " + definition + ".")

glossary['string'] = 'a sequence of characters enclosed in quotes, representing text'
glossary['integer'] = 'a whole number, either positive or negative, without a decimal point'
glossary['float'] = 'a number that has a decimal point'
glossary['tuple'] = 'an ordered, immutable collection of items, typically enclosed in parentheses'
glossary['set'] = 'an unordered collection of unique items, often used for membership testing and eliminating duplicates'

for term, definition in glossary.items():
    print("\n" + term.title() + " - " + definition + ".")

##########

major_rivers = {'nile': 'egypt',
'amazon': 'peru',
'yangtze': 'china'
}

for river, country in major_rivers.items():
    print("\n The " + river.title() + " runs through " + country.title() + ".")

for river in major_rivers.keys():
    print(river.title())

for country in major_rivers.values():
    print(country.title())

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }

poll = ['sarah', 'anna', 'jen', 'john', 'carrie']
for name in poll:
    if name in favourite_languages.keys(): # returning keys is the default, so don't HAVE to specify .keys()
        print(name.title() + ", thank you for taking the poll!")
    
    else:
        print(name.title() + ", please take the poll.")

    