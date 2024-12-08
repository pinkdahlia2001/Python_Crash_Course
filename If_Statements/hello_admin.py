usernames = []

if usernames:
    for username in usernames:
       if "admin" in username:
           print("Hello admin, would you like to see a status report?")
       else:
           print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")


#########

current_users = ['cool_cat23', 'adventure_guru', 'tech_lover91', 'starlight_dreamer', 'pizza_master_77']
new_users = ['Cool_cat23', 'ninja_master88', 'cosmic_spark', 'midnight_rider7', 'TECH_LOVER91']

if new_users:
    for new_user in new_users:
        if new_user.lower() in [current_user.lower() for current_user in current_users]: # convert all new usernames to lowercase.
            print(new_user + " is not available.")
        else:
            print(new_user +  " is available.")


###########

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if numbers:
    for number in numbers:
        if number == 1:
            print(str(number) + "st.")
        elif number == 2: 
            print(str(number) + "nd.")
        elif number == 3:
            print(str(number) + "rd.")
        else: 
            print(str(number) + "th.")
