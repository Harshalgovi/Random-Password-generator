import random


print(
'''=====================================
        PASSWORD GENERATED
=====================================''')

while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length < 1:
            print("Please enter a positive integer for the length.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")



while True:
    uppercase = input("Include uppercase letters? (y/n): ").lower()
    if uppercase == "y" or uppercase == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    lowercase = input("Include lowercase letters? (y/n): ").lower()
    if lowercase == "y" or lowercase == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    numbers = input("Include numbers? (y/n): ").lower()
    if numbers == "y" or numbers == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    special = input("Include special characters? (y/n): ").lower()
    if special == "y" or special == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
collection = [lowercase_letters, uppercase_letters, digits, special_characters]


collection = ""
if lowercase == "y":
    collection += lowercase_letters

if uppercase == "y":
    collection += uppercase_letters

if numbers == "y":
    collection += digits

if special == "y":
    collection += special_characters


password = ""
for x in range(length):
    password += random.choice(collection)
# print(f"Your Password is: {password}")
print("=" * 40)
print("🔐 YOUR GENERATED PASSWORD 🔐")
print("=" * 40)
print(f"                 {password}            ")
print("=" * 40)




print('=====================================')