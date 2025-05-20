"""Displays a users privileges."""

from admin_1 import User

class Privileges():

    def __init__(self, privileges=None):
        """Initialise the privileges attributes."""
        
        if privileges is None:
            privileges = ['can add post', 'can delete post', 
                           'can ban user', 'can modify content']
        self.privileges = privileges
    
        
        
    def show_privileges(self):
        """Prints a simple list of admin privileges."""
        print("Admins have the following privileges: " + (', '.join(self.privileges)) + ".")


class Admin(User):

    def __init__(self, first_name, last_name, city, country, age="", sex=""):
        """Initialise the attributes of the parent class and the flavours."""
        super().__init__(first_name, last_name, city, country, age, sex)
       
       
        self.privileges = Privileges()