# Make a list called sandwich_orders and fill it w/ names of various sandwiches.
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order,
# e.g. I made your tuna sandwich.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['meatball marinara', 'turkey and ham', 'chicken parmesan', ' philly cheesesteak']
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print("We're preparing your " + preparing_sandwich.title() + " sandwich.")
    finished_sandwiches.append(preparing_sandwich)

for finished_sandwich in finished_sandwiches:
    print("Your " + finished_sandwich.title() + " sandwich has finished being prepared.")

# 1. Create a list called sandwich_orders that includes at least three 'pastrami' sandwiches.
# 2. Print a message informing the user that the deli has run out of 'pastrami' sandwiches.
# 3. Use a while loop to remove all occurrences of 'pastrami' from the sandwich_orders list.
# 4. Ensure no 'pastrami' sandwiches end up in the finished_sandwiches list.
# 5. Create an empty list called finished_sandwiches.
# 6. Add all remaining sandwiches from sandwich_orders to finished_sandwiches.
# 7. Print the contents of finished_sandwiches, showing the sandwiches that have been made.

sandwich_orders = ['pastrami', 'vegetable deluxe', 'pastrami', 'meatballs', 'ploughmans']
finished_sandwiches = []
print("Unfortunately the deli has run out of all pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print("We're preparing your " + preparing_sandwich.title() + " sandwich.")
    finished_sandwiches.append(preparing_sandwich)

for finished_sandwich in finished_sandwiches:
    print("Your " + finished_sandwich.title() + " sandwich has finished being prepared.")



