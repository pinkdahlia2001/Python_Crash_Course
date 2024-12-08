# To check whether a particular value is already in a list, use the keyword "in"

requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings) # True
print("pepperoni" in requested_toppings) # False

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users: 
    print(user.title() + ", you can post a response if you wish.")
# can be used to find out if a value is not in a list by using the key words "not in"

# Boolean expression = a conditional test.
# Boolean values can be either 'true' or 'false'.

game_active = True
can_edit = False

