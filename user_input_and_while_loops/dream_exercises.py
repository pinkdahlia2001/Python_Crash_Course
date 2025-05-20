places =  {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("\nIf you could go anywhere in the world, where would you go? ")

    places[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print('\n---POLL RESULTS---') 
for name, place in places.items():
    print(name.title() + " would like to go to " + place.title() + "!")