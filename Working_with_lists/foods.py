my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:] # the slicing index [:] without any indexes copies the whole list.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

# If you don't use [:] when copying a list, and instead just use =, you didn't store a copy of the first list into the second list.
# Any new items appended or inserted will be identical in both lists if you don't use [:]
