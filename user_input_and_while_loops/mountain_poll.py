responses = {} # empty dictionary

# Set a flag to indicate that polling is active. As long as active, while loop will keep running.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\n What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response # name is the key, response is the value.

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")