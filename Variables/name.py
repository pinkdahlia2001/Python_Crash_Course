name = "ada lovelace"
print(name.title())
# The . after the name variable tells Python to make the title() method act on the variable 'name'.
# Parentheses follow because methods, which title() is, often need additional info to do their work.
# title() makes egery word begin w/ a capital letter.

name = "Ada Lovelace"
print(name.upper())
print(name.lower())
# lower() method is useful for storing data, when you don't want to trust the capitalisation that the users provide.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
# You combine strings by using +. " " provides a space. 
# The combining of strings is known as concatenation.

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("Python")
print("\tpython") 
# \t adds a whitespace.

print("Languages:\nPython\nC\nJavascript") 
# \n adds a newline to string

print("Languages:\n\tPython\n\tC\n\tJavascript") # Combo of \n and \t

favourite_language = "python "
print(favourite_language)

print(favourite_language.rstrip())
# rstrip() removes whitespace from the right side, only when this method is used though.

# To permanently remove whitespace:
favourite_language = "python "
favourite_language = favourite_language.rstrip()
print(favourite_language)

# Use lstrip() to strip whitespace from the left side of a string
# Use strip () to strip whitespace from both sides at once.