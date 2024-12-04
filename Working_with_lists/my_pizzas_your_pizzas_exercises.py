my_pizzas = ["margherita", "miss italia", "pepperoni", "meat feast"]
print(my_pizzas)
rickys_pizzas = my_pizzas[:]

my_pizzas.append("nutella")
rickys_pizzas.append("puttanesca")

print("My favourite pizzas are:")
for values in my_pizzas:
    print(values.title())

print("\nRicky's favourite pizzas are:")
for pizzas in rickys_pizzas:
    print(pizzas.title())