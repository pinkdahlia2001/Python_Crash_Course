# .remove() allows you to remove a value one at a time
# however when you want to remove all instances of a value from a list, you have to run a while loop and then use .remove()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat') 

print(pets)