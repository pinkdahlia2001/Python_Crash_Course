# to exit a while loop immediately without running any remaining code in the loop, regardless of the results of the conditional test, use "break"
# break directs the flow of the program, allows you to control which lines of code are executed and which aren't.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True: # will run forever unless it reaches a break statement.
    city = input(prompt)

    if city == 'quit':
        break

    else: 
        print("I'd love to go to " + city.title() + "!")