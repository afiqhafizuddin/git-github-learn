name = 'Afiq Hafizuddin bin Zainal'

print(name)
print('Hello, world')

def check_name(name):
    if len(name) >= 15:
        print('Invalid username')
    elif len(name) <= 3:
        print('Invalid username')
    else:
        print("Valid username")

check_name(name)

# string modification

def double_get(word):
    return str(word) + str(" ") + str(word) + str(" ")+ str(len(word))
print(double_get('Hello'))
print(double_get("Afiq Hafizuddin bin Zainal"))
print(double_get("JavaScript"))