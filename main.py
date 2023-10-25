option = 1
password = ""
ret = ""
dec = ""

while option == 1 or option == 2:
    # Printing the menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    # Selecting an option from the menu
    option = int(input("Please enter an option:"))

    if option == 1:
        password = input("Please enter your password to encode:")  # Store the password as a string
        encoded_password = ""

        for char in password:
            encoded_char = str((int(char) + 3) % 10)
            encoded_password += encoded_char

        print("Your password has been encoded and stored!")
        ret = encoded_password

    if option == 2:
        decoded_password = ""
        for char in password:
            decoded_char = str((int(char) + 10 - 3) % 10)
            decoded_password += decoded_char
        print(f"The encoded password is {ret} and the original password is {decoded_password}")