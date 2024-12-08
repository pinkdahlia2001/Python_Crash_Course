alien_colour = "green"

if alien_colour == "green":
    print("You have just earned 5 points!")


alien_colour = "green"

if alien_colour == "red":
    print("You have just earned 5 points!")

#########

alien_colour = "yellow"

if alien_colour == "green":
    print("You have just earned 5 points for shooting the alien!")

else:
    print("You have just earned 10 points!")


alien_colour = "green"

if alien_colour == "green":
    print("You have just earned 5 points for shooting the alien!")

else:
    print("You have just earned 10 points!")

#########

alien_colour = "green"

if "green" in alien_colour:
    print("You have earned 5 points.")
elif "yellow" in alien_colour:
    print("You have earned 10 points.")
else: 
    print("You have earned 15 points.")

alien_colour = "yellow"

if "green" in alien_colour:
    print("You have earned 5 points.")
elif "yellow" in alien_colour:
    print("You have earned 10 points.")
else: 
    print("You have earned 15 points.")


alien_colour = "red"

if "green" in alien_colour:   # tbh dont use this method.
    print("You have earned 5 points.")
elif "yellow" in alien_colour:
    print("You have earned 10 points.")
else: 
    print("You have earned 15 points.")


############

age = 4

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else: print("You are an elder.")


###########

favourite_fruits = ["mango", "avocado", "peaches"]

if "mango" in favourite_fruits:
    print("You really like mangoes!")
if "avocado" in favourite_fruits:
    print("You really like avocados!")
if "peaches" in favourite_fruits:
    print("You really like peaches!")
if "bananas" in favourite_fruits:
    print("You really like bananas!")
if "strawberry" in favourite_fruits:
    print("You really like strawberries!")

