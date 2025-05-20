favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }

print("Sarah's favourite language is " + # + is a concatenation operator
      favourite_languages['sarah'].title() +
      ".")
print(favourite_languages['sarah']) # asking for the value in the dictionary

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

for name in favourite_languages.keys(): # using .keys() pulls all the keys from the dictionary
    print(name.title())

# looping through keys is the default behaviour when looping through a dictionary, so using:
# for name in favourite_languages: would produce the same output.

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
              ", I see your favourite language is " +
              favourite_languages[name].title() + "!")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

# To return items in order:
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# ^ this pulls all values from a dictionary without checking for repeats.

# To pull values without repetition, you use set():
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())