alien_0 = {'color': 'green', 'points': 5} # key value = color/points, associated value = green/5
print(alien_0['color'])
print(alien_0['points'])
# Use curly brackets to create dictionaries!
# Use square brackets to access keys and lists.

# a python dictionary - a collection of key-value pairs.
# a key's value can be any object created in python, including numbers, strings, lists, other dictionaries.

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0 # how to add new key-values and associated values to a dictionary.
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {} # creating a dictionary with 0 values, and adding them later.
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + '.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
print(alien_0['x_position'])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0) # deleting the key points gets rid of the associated values too. 

