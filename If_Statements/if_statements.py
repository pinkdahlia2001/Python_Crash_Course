age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: # If the first test returns as false, then the else block will be executed.
    print("Sorry, you are too young to vote.")
    print("Please register as soon as you turn 18.")

########## if-elif-else chain ############

# Python only executes one block in an if-elif-else chain. It runs each conditional test in order until one passes.
# When a test passes, the following code blocks are skipped.
# e.g. An amusement park that charges different rates for different age groups:
# - Admission for anyone under the age of 4 is free.
# - Between ages 4-18 is £5.
# - Anyone 18 or older is £10.

age = 12
if age < 4:
    print("Your admission cost is £0.")
elif age < 18: # this line is saying "age is between 4 and 18" without explicitly stating it.
    print("Your admission cost is £5.")
else: # If both if and elif fails, then else is printed.
   print("Your admission cost is £10.")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is £" + str(price) + ".")

###########

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: # younger than 65.
    price = 10
else: 
    price = 5
print("Your admission cost is £" + str(price) + ".")

# else blocks at the end are not required. else blocks are fallback statements.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5


print("Your admission cost is £" + str(price) + ".")

####### Testing multiple conditions #######

# if-elif-else chain blocks are only appropriate to use when you need just one test to pass, as once one does, the rest of the tests are skipped.
# to check all conditions of interest, a series of simple if statements can be used.
# this technique makes sense when more than one condition can be true, and you want to act on every condition that is true.

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperonis.")
if 'extra cheese' in requested_toppings: # all tests run regardless of whether the previous test passed or not.
    print("Adding extra cheese.")
print("\nFinished making your pizza!")