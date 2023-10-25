
def encode(password):
    encoded_password = ""
    for char in password:
        encoded_char = str((int(char) + 3) % 10)
        encoded_password += encoded_char
    return encoded_password

def decode(password):
    decoded_password = ""
    for char in password:
        decoded_char = str((int(char) - 3) % 10)
        decoded_password += decoded_char
    return decoded_password

def main():
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

            ret = encode(password)
            print("Your password has been encoded and stored!")


        if option == 2:
            #ADDED BY ISAAC
            print(f"The encoded password is {ret} and the original password is {decode(ret)}")

if __name__ == "__main__":
    main()