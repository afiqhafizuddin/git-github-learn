from os import name


name = 'afiq hafizuddin bin zainal'

def check_name(name):
    if len(name) >= 15:
        print('Invalid username')
    elif len(name) <= 3:
        print('Invalid username')
    else:
        print("Valid username")

check_name(name)