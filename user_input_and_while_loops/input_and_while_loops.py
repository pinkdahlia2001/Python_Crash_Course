message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# input() allows the user to input a response in the terminal, and press enter. 
# Pressing enter in this instance causes the program to repeat the message back.

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we personalise the messages that you see."
prompt += "\nWhat is your first name? " # += takes the string that was stored in prompt and adds the new string onto the end.
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
age = int(age) #use integer when trying to use numbers to do a numerical comparison.
print(age >= 18)

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")