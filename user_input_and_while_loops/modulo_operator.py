#### MODULO OPERATOR ########
# % is the modulo operator, which divides one number by another number and returns the remainder.
# e.g. Divide 17 by 4:
# 17 ÷ 4 = 4 with a remainder of 1 (because 4 * 4 = 16, and 17 - 16 = 1).
# Multiply the quotient by the divisor:
# 4 * 4 = 16.
# Subtract that result from 17:
# 17 - 16 = 1.
# So, 17 % 4 = 1, which is the remainder.

# Modulo operator tells you what the remainder is when you divide one number by another, NOT how many times a number is divisible.
# When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

