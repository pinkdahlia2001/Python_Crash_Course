# Slicing allows for easy access to extract, modify, or reverse sequences with minimal code.
# More efficient and readable than using loops.

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) # This returns elements 0, 1, and 2. So the first 3.
print(players[1:4]) # The slice starts at element 1, basically printing the 2nd, 3rd and 4th elements.

# sequence[start:end:step]
# start is the index where the slice begins, meaning it includes the element.
# end is the index where the slice ends, and is exclusive so it is not included in the element.

print(players[:4]) # if no start is indicated, Python automatically starts at the beginning of the list.

print(players[2:]) # allows for slicing from index 2 to end of the list

print(players[-2:]) # starts from second from last index.

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title()) # Only the first three names are looped.

