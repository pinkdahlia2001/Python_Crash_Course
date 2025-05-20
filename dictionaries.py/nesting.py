# nesting - storing a set of dictionaries in a list, or a list of items as a value in a dictionary.
# able to nest a set of dictionaries in a list, a list of items inside a dictionary, or a dictionary inside another dictionary.

alien_0 = {'color': 'green',
'points': 5}
alien_1 = {'color': 'yellow',
'points': 10}
alien_2 = {'color': 'red',
'points': 15}

aliens = [alien_0, alien_1, alien_2] # the dictionaries in a list.

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30): # range(30) means the loop will run 30 times from 0-29, creating a new dictionary.
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) # after each alien is created, it is appended/added to the list.

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]: # returns the first 5 aliens in the list
    print(alien)
    print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens))) # len gives the total number of aliens in the list