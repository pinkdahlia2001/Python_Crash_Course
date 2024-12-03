for value in range(1,21):
    print(value)

million = list(range(1,1000000))
print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)


threes = [value for value in range(3,31,3)]
print(threes)

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes) # move the print function outside of the loop

cubes = [value**3 for value in range(1,11)]
print(cubes)