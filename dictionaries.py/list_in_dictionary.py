# Store info about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# summarise the order.
print("You ordered a " + pizza['crust'] +"-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']: # because the toppings are stored in a list, so a loop is needed to go through each item.
    print("\t" + topping)

#######

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favourite_languages.items():
    if len(languages) > 1: 
        print("\n" + name.title() + "'s favourite languages are:") 
    else:
        print("\n" + name.title() + "'s favourite language is:")
    for language in languages:
        print("\t" + language.title())