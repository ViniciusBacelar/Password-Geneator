import random

print('Welcome to your Password Generator!')

string_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().?,1234567890'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(string_characters)
    print(passwords)
