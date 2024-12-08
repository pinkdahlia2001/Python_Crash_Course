# Looping allows you to take the same action, or set of actions with every item in a list.
# Automates repetitive tasks
magicians = ["alice", "david", "carolina"]
for magician in magicians:  #  this line tells Python to retrieve the first value from the list magicians and store it in the variable region.
    print(magician)  # prints the current value of magician. and then returns back to the first line of the loop for all items in the list.
      # a.k.a. for every magician in the list, print the magician's name.
# The for loop in this case is used to pull a name from the list magicians, and then print it. And to repeat it once for every name on the list.
# Once there are no more values in the list, Python moves on to the next line in the program.

magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
# Every indented line following the line for magician in magicians is considered inside the loop, and is executed once for each item.
# Can do as many functions as you want.

# \n creates a new line after each pass through of the loop.
#e.g. using a for loop to initialise a game by running through a list of characters and displaying each character on the screen. Then add an unindented block to display the Play NoW button after all characters have been drawn to the screen.

# ALWAYS INDENT THE LINE AFTER THE FOR STATEMENT IN A LOOP.
# ALWAYS REMEMBER TO ADD A COLON AT THE END OF FOR STATEMENT.


