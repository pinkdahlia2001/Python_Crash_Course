car = "audi"
print(car == "bmw") # double equal sign "==" returns True if values on the left and right side of the operators match, and False if they don't.
# In the example above, Python would return false.
# A single equal sign '=' is a statement, while a "==" asks a question e.g. is the value of car = to BMW?

print(car=="Audi") # Testing for equality is case sensitive in Python. 
# e.g. two values with different capitalisation are not considered equal.

car = "Audi"
print(car.lower() == "audi") 
# You can convert the variables value to lower case before doing the comparison so that the test returns as true.
# .lower() does not change how the value is orginally stored.
# e.g. a website using a conditional test like this to ensure every user has a truly unique username, not just a variation on the capitalisation of another person's username.
# cont: the u/n would be temporarily converted to lowercase and compared to lwoercase versions of all existing usernames.

