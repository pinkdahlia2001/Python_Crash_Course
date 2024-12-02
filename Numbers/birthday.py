age = 23
message = "Happy " + age + "rd Birthday" # This is a type error, you must specifically specify that you want Python to use the integer as a string of characters.
print(message)


age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message) # This is correct!