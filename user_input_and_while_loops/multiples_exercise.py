ten = input("Pick a number, and I will tell you whether it is a multiple of 10 or not ")
ten = int(ten)

if ten % 10 == 0:
    print(str(ten) + " is a multiple of ten!")
else:
    print(str(ten) + " is not a multiple of ten.")