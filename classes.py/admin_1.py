"""A class used to collect user info."""

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