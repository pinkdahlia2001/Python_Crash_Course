# For a program that should run only as long as many conditions are true, one variable that determines whether or not the whole program is active can be defined.
# This variable is called a flag, and acts as a signal to the program.
# You can set the program to run while the flag is set to True, and stop running when any several events set the value of the flag to false.
# this means that the while statement needs to only check whether or not the flag is currently True.

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True # program starts in an active state.
while active:
    message = input(prompt)

    if message == 'quit': # checks the value of the user input once it's been inputted. entering quit sets the flag to false, stopping the while loop.
        active = False
    else:
        print(message)
# writing it this way allows for way more tests to be added, for events that can cause the flag to be false.

