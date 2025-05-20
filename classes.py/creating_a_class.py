class Dog(): # the class is defined as dog. Capitalised names refer to classes in python. Empty parenthesis because the class is created from scratch.
    """A simple attempt to model a dog."""

    def __init__(self, name, age): # A function that is part of a class is a method.
        """Initialise name and age attributes.""" # __init__ has 3 parameters. Self paremeter must come first before other parameters because it is required in the method definition.
        self.name = name # any variable prefixed with self is available to every method in the class.
        self.age = age # variables accessible through instances like this are called attributes.
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# __init__ is a special method Python runs automatically whenever we create a new instance based on the Dog class.
# this method has 2 leading underscores and two trailing underscores, which helps prevents Python's default method names from conflicting with method names.
# functions are called methods when they're enclosed in classes.

my_dog = Dog('willie', 6) # creates a dog with the name willie who is 6 y.o. Python calls __init__ in Dog with the arguments willie and 6.
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# the __init__ method creates an instance representing this particular dog and sets the name and age attributes using the values provided.
# __init__ method has no explicit return statement, but Python automatically returns an instance representing this dog.
# this is stored in the variable my_dog.

# Accessing attributes #

# to access the attributes of an instance, you use dot notation.
# btw name is the instance :)
# my_dog.name()

# Calling methods #

my_dog.sit() # after creating instances from the class Dog, dot notation can be used to call any method defined in Dog.
my_dog.roll_over()

