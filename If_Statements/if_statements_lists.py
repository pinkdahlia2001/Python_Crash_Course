requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings: # used first as we assumed that the list has items.
    if requested_topping == 'green peppers': # checks to see if person requested green peppers.
        print("Sorry, we are out of green peppers right now.")
    else: # ensures all other toppings will be added to the pizza.
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings: # 'if' checks the elements in the list
    for requested_topping in requested_toppings: #  If the list is not empty and you know this, the 'for' loop iterates over each item in the list.
        print("Addings " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")
#  use if first if you're not sure that there are any items in the list.

##### Using multiple lists ######

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")