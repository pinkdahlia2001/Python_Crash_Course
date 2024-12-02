cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort() # sort() method puts the items in the list in alphabetical order, unless specified otherwise. BTW permamently.
print(cars)

cars.sort(reverse=True) # sort(reverse=True) puts the items in the list in reverse alphabetical order. BTW permanently.
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #sorted() function allows for temporary sorting of the list without affecting the actual order.

print("\nHere is the original list again:")
print(cars) 

print(cars)
cars.reverse() # reverse() reverses the original order of the list (not necessarily in reverse alphabetical order. PERMANENT BTW)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars)) #len() counts the length of a list.
