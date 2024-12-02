bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles)
# square brackets [] denote a list.

print(bicycles[0]) # This lists just one item from the list, the first.
print(bicycles[0].title())
# Index positions start at 0, not 1. So the 2nd item has an index of 1.
# To get any element you want from the list, subtract 1 from the index.

print(bicycles[-1]) # -1 is used to return the last item in a list.
# -2 returns the second last, -3, the third last, and so forth....

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)