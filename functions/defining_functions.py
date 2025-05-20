def greet_user(): # def informs Python that you're defining a function. The parenthesis holds the info needed. No info needed to do the job, so its parentheses are empty.
    """Display a simple greeting.""" # this is a docstring, which describes what the location does. Uses triple quotes, which is what Python looks for when generating documentation for functions in programs.
    print("Hello!") # this is the only actual line of code in the body of this function.
greet_user()
# A function call tells Python to execute the code in the function.
# To call a function, you write the name of the function, followed by any necessary info in parentheses

def greet_user(username): # def is used to define a function in Python. greet_user is the name of the function. The name should describe what the function does.
    """Display a simple greeting.""" # all indented lines make up the body of the function
    print("Hello, " + username.title() + "!")

greet_user('jesse') # the function is being called by its name. 'jesse' is the argument passed to the function. It replaces the username parameter in the function definition.


# (username) is the parameter. A parameter is a placeholder that the function expects to receive as input when called.
# """""""" docstrings help others understand the purpose of the function.

greet_user('sarah') # sarah here is the username, it is an argument that is passed from the function call to a function.
greet_user('hollie')

def display_message():
    """Displays a message about what is being learned in this chapter."""
    print("In this chapter we are learning about writing functions.")

display_message()


def favourite_book(title):
    """Displays a simple message about a favourite book"""
    print("One of my favourite books is " + title.title() + ".")

favourite_book('lily alone')
favourite_book('haunting adeline')