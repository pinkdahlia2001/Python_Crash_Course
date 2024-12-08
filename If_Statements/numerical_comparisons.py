age = 18
print(age == 18)

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21) # age is less than 21, so this returns true.
print(age <=21) # age is less than or equal to 21
print(age > 21) # age is more than 21, this is false, so returns false.
print(age >= 21) # age is less than or equal to 21, this is false, so returns false.


# Checking for multiple conditions

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # this returns as false, because age_1 is not equal to or less than 21

age_1 = 22
print((age_0 >= 21) and (age_1 >= 21)) # this returns as true because age 1 is now equal to or over 21.
# Both individual tests must pass for Python to return true.

# Using or to Check Multiple Conditions #

# using or allows you to check multiple conditions, but passes when either one or both individual tests pass.
# Python will only return false on an "or" statement if both tests are false.

age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >=21)) # This prints as true even though age_1 is not equal to or more than 21.

age_0 = 18
print((age_0 >= 21) or (age_1 >=21)) # This returns false as neither ages are equal to or over 21.



