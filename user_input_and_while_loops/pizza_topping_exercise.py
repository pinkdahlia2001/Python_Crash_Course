toppings = "We're making your delicious pizza!"
toppings += "\nPlease enter your desired topping: "
desired_topping = ""
while desired_topping != 'quit':
    desired_topping = input(toppings)
    print(desired_topping)
    if desired_topping != 'quit':
        print("Adding " + desired_topping.title() + " to your pizza!")

if desired_topping == 'quit':
    print("Your pizza is now being prepared and put in the oven.")


