# the for loop executes a block of code once, while a while loop runs as long as, or while a certain condition is true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 
    # += is shorthand ofr current_number = current_number + 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. " #+= adds (concatenates) the second string ("\nEnter 'quit' to end the program. ") to the existing string prompt
message = "" # stores whatever value the user enters. As the message is initially empty, Python enters the loop.
while message != 'quit': # != means NOT EQUAL
    message = input(prompt)
    print(message)

if message != 'quit':
    print(message)

# += The purpose of using += is to build up the prompt string in stages, adding additional information to it without overwriting the initial value.

