pizza = "margherita"
print('Is pizza == "margherita"? I predict True.')
print(pizza == 'margherita')

print('\nIs pizza == "pepperoni"? I predict False.')
print(pizza == "pepperoni")

#########

colour = "hotpink"
print('Is colour == "hotpink"? I predict True.')
print(colour == "hotpink") 

print("\nIs colour = 'babyblue'? I predict False.")
print(colour == "babyblue") 

#########

country = "norway"
print('Is country =="norway"? I predict True.')
print(country == "norway")

print('Is country == "Norway"? I predict False.')
print(country == "Norway")

#########

fruit = "banana"
print('Is fruit =="banana"? I predict True.')
print(fruit == "banana")

print('Is fruit == "apple"? I predict False.')
print(fruit == "apple")

###########

vegetable = "courgette"
print('Is vegetable =="courgette"? I predict True.')
print(vegetable == "courgette")

print('Is vegetable == "zucchini"? I predict False.')
print(vegetable == "zucchini")


###########

drink = "cocacola"
print('Is drink =="cocacola"? I predict True.')
print(drink == "cocacola")

print('Is drink == "water"? I predict False.')
print(drink == "water")

###########

gluten_free = "yes"
if gluten_free == "yes":
    print("Gluten free pizza coming right up!")
if gluten_free != "no":
    print("Pizza with Garlic and Herb crust coming right up!")

##########

new_username = "Riccardo.Dalleva93"
if new_username.lower() == "riccardo.dalleva93":
    print('Sorry, ' + new_username.lower() + ' is already taken. Please try another username.')

if new_username.lower() != "Riccardo.Dalleva93":
    print(new_username + ' is available.')

age = 18

print(age > 21)
print(age < 30)
print(age >= 23) 
print(age <= 17)
print(age == 19)
print((age < 23) or (age > 17))

##############

allergies = ["tree nuts", "peanuts", "shellfish", "wheat"]
allergy = "soy"
allergy2 = "pineapple"

if allergy not in allergies:
    print(allergy.title() + " is not a listed allergen on this list.")

allergy = "peanuts"
if allergy in allergies:
    print(allergy.title() + " is a listed allergen on the list.")

if allergy or allergy2 in allergies: 
    print("I'm sorry, however this food contains allergens that you are allergic to.")

if allergy and allergy2 not in allergies:
    print("This list does not contain all of your allergens.")



