import random


print(
'''=====================================
        PASSWORD GENERATED
=====================================''')

history = []

while True:





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
    history.append(password)
    
    print("=" * 40)
    print("🔐 YOUR GENERATED PASSWORD 🔐")
    print("=" * 40)
    print(f"{password}")
    print("=" * 40)






    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    special_count = 0

    for char in password:

        if char.isupper():
            uppercase_count += 1

        elif char.islower():
            lowercase_count += 1

        elif char.isdigit():
            number_count += 1

        else:
            special_count += 1



    strength = ""
    if (length >= 12 and uppercase_count >= 2 and lowercase_count >= 2 and number_count >= 2 and special_count >= 2):
        strength = "Strong 🟢"
    elif (length >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and number_count >= 1 and special_count >= 1):
        strength = "Moderate 🟡"
    else:
        strength = "Weak 🔴"

    print(f"Password Strength: {strength}")


    view_history = input("Do you want to view password history? (y/n): ").lower()


    if view_history == "y":
        print("===========================")
        print("PASSWORD HISTORY")
        print("===========================")

        count = 1

        for password in history:

            print(f"{count}. {password}")
            count += 1

    answer = input("do you want to generate another password? (y/n): ")

    if answer == "y":
        continue

    elif answer == "n":
        print("Thank you for using the password generator!")
        exit()
