current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# Because the current_number is less than 10, Python enters the while loop, and increments the current_number by 1.
# the if statement checks the modulo of current_number and 2. If the modulo number is 0, the continue statement tells Python to ignore the rest of the loop and return to the beginning.
# if the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.

x = 1
while x <= 5:
    print(x)
    x += 1 # (x = x + 1, add 1 to the current number and then assign it back)

# to escape an infinite loop, press CTRL-C or close the terminal window.
# to avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to.
# make sure at least one part of the program can make the loop's condition False or cause it to reach a break statement.