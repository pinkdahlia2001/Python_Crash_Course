# when you pass a list to a function, the function gets direct access to the contents of the list.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# recap: A for loop is used to iterate over a sequence (like a list, tuple, string, or range of numbers) and execute a block of code multiple times.

# MODIFYING A LIST IN A FUNCTION #

# When passing a list to a function, the function can modify the list.
# Any changes made to the list by the function are permanent, allowing you to work efficiently when when dealing with large amounts of data.

# e.g. a company that creates 3D printed models of designs that users submit.
# Desings that need to be printed are stored in a list, and after being printed are moved to a seprate list.


from printing_functions import print_models as pm, show_completed_models as sc

unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_design, completed_models)
sc(completed_models)

# the first function prints each design, while the second one displays the completed models.

# PREVENTING A FUNCTION FROM MODIFYING A LIST #

# e.g. you start with a list of unprinted designs and write a function to move them to a list of completed models.
# You may decide that even though you've printed all the designs, you want to keep the original list of unprinted designs for your records.
# because all the design names were moved out of unprinted_designs, the list is now empty, and the empty list is the only version remaining, the original is gone.
# in this case, you can address the issue by passing the function a copy of the list, not the original.

# how to send a copy of a list to a function:
# function_name(list_name[:])
# the slice notation [:] makes a copy of the list to send to the function.
pm(unprinted_design[:], completed_models)
# the list of completed models fills up w/ the names of printed models, but the original list of unprinted designs remains empty.

# EXERCISES #


def show_magicians(magicians):
    for magician in magicians:
        print("\n" + magician.title())

magicians = ['houdini', 'copperfield', 'blaine', 'henning']
show_magicians(magicians)

# 8-10: Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician's name. 
# Call show_magicians to see that the list has actually been modified.

def show_magicians(magicians):
    for magician in magicians:
        print("\n" + magician.title())

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['houdini', 'copperfield', 'blaine', 'henning']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)


# Call the function make_great() with a copy of the list of magicians' names. Because the original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the great added to each magician's name.

def show_magicians(magicians):
    for magician in magicians:
        print("\n" + magician.title())

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['houdini', 'copperfield', 'blaine', 'henning']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

#####

def show_team_members(team_members):
    for team_member in team_members:
        print("\n" + team_member.title())

team_members = ['john', 'alice', 'bob', 'eve']

show_team_members(team_members)

def promote_team_members(team_members):
    promoted_team_members = []

    while team_members:
        team_member = team_members.pop()
        promoted_team_member = team_member + " (Promoted)"
        promoted_team_members.append(promoted_team_member)

    return promoted_team_members

    for promoted_team_member in promoted_team_members:
        team_members.append(promoted_team_member)


show_team_members(team_members)
promoted_team_members = promote_team_members(team_members[:])
show_team_members(promoted_team_members)
