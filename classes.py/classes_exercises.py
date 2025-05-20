class Restaurant():
    """Prints simple information about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the name and cuisine of the restaurant."""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Prints that the cuisine is open."""
        print(self.restaurant_name.title() + " is open.")

restaurant = Restaurant("mcdonald's", "american")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_0 = Restaurant("frankie and benny's", "italian-american")
restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

restaurant_1 = Restaurant("water under the bridge", "british")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant("nandos", "south african")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()


####

class User():
    """Collects user info."""
    def __init__(self, first_name, last_name, city, country, age = "", sex = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.country = country
        self.age = age
        self.sex = sex

    def describe_user(self):
        """Prints collected user info."""
        print("\nName: " + self.first_name.title() + " " + self.last_name.title())
        print("Location: " + self.city.title() + ", " + self.country.title())
        
        if self.age != "":
            print("Age: " + str(self.age))
        else:
            print("Age: Unknown")

        if self.sex != "":
            print("Sex: " + self.sex.title())
        else:
            print("Sex: Unknown")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + " " + self.last_name.title() + "!")


john = User("john", "doe", "new york", "america", sex = "male")
john.describe_user()
john.greet_user()

max = User("maximilian", "mund", "munich", "germany", 33, "male")
max.describe_user()
max.greet_user()

jane = User("jane", "doe", "berlin", "germany", 33, "female")
jane.describe_user()
jane.greet_user()

alice = User("alice", "johnson", "sydney", "australia")
alice.describe_user()
alice.greet_user()

amara = User("amara", "singh", "mumbai", "india", 45)
amara.describe_user()
amara.greet_user()


####

class Restaurant():
    """Prints simple information about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # this is an attribute.

    def describe_restaurant(self):
        """Prints the name and cuisine of the restaurant."""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Prints that the cuisine is open."""
        print(self.restaurant_name.title() + " is open.")

    def read_number_served(self):
        """Reads the number of customers served."""
        print(self.restaurant_name.title() + " has served " +
               str(self.number_served) + " customers.")
        
    def set_number_served(self, customers):
        """Allows user to manually update number served."""
        self.number_served = customers

    def increment_number_served(self, customer_no):
        """Adds the given amount to amount of customers served."""
        self.number_served += customer_no
        


restaurant = Restaurant("mcdonald's", "american")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_number_served()

restaurant.set_number_served(2000000000)
restaurant.read_number_served()
restaurant.increment_number_served(5405493)
restaurant.read_number_served()


 ########

class User():
    """Collects user info."""
    def __init__(self, first_name, last_name, city, country, age = "", sex = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.country = country
        self.age = age
        self.sex = sex
        self.login_attempt_count = 0

    def describe_user(self):
        """Prints collected user info."""
        print("\nName: " + self.first_name.title() + " " + self.last_name.title())
        print("Location: " + self.city.title() + ", " + self.country.title())
        
        if self.age != "":
            print("Age: " + str(self.age))
        else:
            print("Age: Unknown")

        if self.sex != "":
            print("Sex: " + self.sex.title())
        else:
            print("Sex: Unknown")

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + " " + self.last_name.title() + "!")


    def show_login_attempts(self):
        print("You have attempted to log in " + str(self.login_attempt_count) + " times.")

    def increment_login_attempts(self, attempt_num = 1):
        self.login_attempt_count += attempt_num  

    def reset_login_attempts(self):
            self.login_attempt_count = 0



amara = User("amara", "singh", "mumbai", "india", 45)
amara.describe_user()
amara.greet_user()
amara.increment_login_attempts()
amara.increment_login_attempts()
amara.increment_login_attempts()
amara.increment_login_attempts()
amara.increment_login_attempts()
amara.show_login_attempts()
amara.reset_login_attempts()
amara.show_login_attempts()
