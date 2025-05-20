# a FOR loop is effective for looping through a list, but a list shouldn't be modified inside a for loop because Python will have trouble keeping track of the items in the list.
# To modify a list as you work through it, use a while loop.
# using while loops with lists and dictionaries allows you to collect, store and organise lots of input to examine and report on later.

# moving items from one list to another.

# Start with items that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users =  []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed ysers.
while unconfirmed_users: # runs as long as list unconfirmed_users is not empty
    current_user = unconfirmed_users.pop() #.pop() removes unverified users one at a time from the end of unconfirmed_users
 # Candace is the last in the unconfirmed_users list, so she is the first to be removed, stored in current_user, and then added to the confirmed_users list.
    print("Verifying user " + current_user.title() + "...")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


