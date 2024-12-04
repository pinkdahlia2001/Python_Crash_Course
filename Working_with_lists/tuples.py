# values that cannot change = immutable
# list containing immutables = tuple
# Cannot insert or remove values from a tuple.
# examples of when tuples are used: storing coordinates.
# to make a list a tuple, you use () instead of [] when creating the list

dimensions = (200, 50) # <--- a tuple!
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) # The content of tuples cannot be modified, but the variables can be reassigned to a new tuple, as shown here.
print("\nModified dimensions:") 
for dimension in dimensions:
    print(dimension)    