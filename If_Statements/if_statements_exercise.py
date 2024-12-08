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