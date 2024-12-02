motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati" # This replaces the first element in the list, can be done to change any value in the list.
print(motorcycles) 

motorcycles.append('harley') # Adds an element to the end of the list.
print(motorcycles)

#######################

apples = []  # This list is empty. It's normal to create an empty list and append items in later.

apples.append('gala')
apples.append('golden delicious')
apples.append('granny smith')
apples.append('bramley')
apples.append('pink lady')
print(apples)

apples.insert(3, 'red delicious') # The insert() method allows for the item to be added at any specified position, remember -1.
print(apples)

del apples[0] # Allows for the deletion of an element at any specified position.
print(apples)

favourite = apples.pop(0)
print("My favourite type of apple is " + favourite.title() + ".")
print(apples)
# the pop() method removes an item in a list at any position but allows you to still work with the item.
# e.g. of times when pop() can be used: in a web app where you want to remove a user from a list of active members and then add their user to a list of inactive members
print(apples)

popped_apples = apples.pop() # Without specifying a position, pop() removes the last item in a list.
print(apples)
print(popped_apples) 

# Use del() to delete if you will not use that item in any way, use pop() if you want to use an item as you remove it.