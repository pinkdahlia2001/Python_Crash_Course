from collections import OrderedDict

favourite_languages = OrderedDict() # No curly brackets needed, the call to OrderedDict() creates an empty ordered dictionary and stores it in favourite_languages.

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
          language.title() + ".")
    

#######

from collections import OrderedDict

glossary = OrderedDict()

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


######

from random import randint

class Die():
    """Prints a randomised number."""

    def __init__(self, sides=6):
        """Initialises sides."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the amount of sides."""
        x = randint(1, self.sides)
        print(x)

dice = Die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()

class Die():

    def __init__(self, sides=10):
        """Initialises sides."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and number of sides."""
        x = randint(1, self.sides)
        print(x)

dice = Die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()


class Die():
    
    def __init__(self, sides=20):
        """Initialises amount of sides."""
        self.sides = sides


    def roll_die(self):
        """Prints a random number between 1, and the amount of sides."""
        x = randint(1, self.sides)
        print(x)

dice = Die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()