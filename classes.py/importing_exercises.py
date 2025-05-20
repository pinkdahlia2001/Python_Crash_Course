from inheritance_exercises import Restaurant, IceCreamStand

eis = IceCreamStand('ice stone', 'gelateria')
eis.get_flavours()


from admin_1 import User
from admin_2 import Privileges, Admin

user_admin = Admin("john", "doe", "paris", "france")
user_admin.privileges.show_privileges()