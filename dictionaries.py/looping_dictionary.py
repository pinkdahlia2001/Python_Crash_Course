user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
          }

for key, value in user_0.items(): # the terms key and value here are variables returning the first and second variable in the tuple, however you can use any variable names.
    print("\nKey: " + key)
    print("Value: " + value)

for k, v in user_0.items(): # .items() returns a list of key-value pairs
    print("\nKey: " + k)
    print("Value: " + v)