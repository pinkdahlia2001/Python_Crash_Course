ticket_info = "The price of your cinema ticket is dependent on your age."
ticket_info += "\n Please enter 'quit' when you are finished."
ticket_info += "\n Please enter your age. "

while True:
    age = input(ticket_info)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free of charge.")
    elif age < 13:
        print("Your ticket is £10.")
    else:
        print("Your ticket is £15.")