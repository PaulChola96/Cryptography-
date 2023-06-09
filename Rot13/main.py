# Author:   [PAUL CHOLA MUMBI]
# Linkedin: [https://www.linkedin.com/in/paul-chola-bwembya-mumbi/]
# Twitter:  [https://twitter.com/PaulChola96]
# Date:     [09/04/2023]
# Program: [rot13]

# Prompt user to choose encryption or decryption mode
mode_algorithm = int(input("Enter 1 to encrypt, or 2 to decrypt: "))

# Prompt user to input message to be encrypted/decrypted
message = input("Enter a message to encrypt or decrypt: ")

if mode_algorithm == 1:
    # If encryption mode is chosen, prompt user to input shift value
    shift = int(input("Enter a shift value: "))
    encrypted_message = ""
    # Iterate over each character in the message and shift its ASCII value by the given shift value
    for char in message:
        if char.isalpha(): # Only shift alphabetic characters
            if char.isupper(): # Handle uppercase letters
                encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
            else: # Handle lowercase letters
                encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else: # Leave non-alphabetic characters as-is
            encrypted_message += char
    print("Encrypted message:", encrypted_message)

elif mode_algorithm == 2:
    # If decryption mode is chosen, prompt user to input the shift value used to encrypt the message
    shift = int(input("Enter the shift value used to encrypt the message: "))
    decrypted_message = ""
    # Iterate over each character in the message and shift its ASCII value by the inverse of the given shift value
    for char in message:
        if char.isalpha(): # Only shift alphabetic characters
            if char.isupper(): # Handle uppercase letters
                decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
            else: # Handle lowercase letters
                decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else: # Leave non-alphabetic characters as-is
            decrypted_message += char
    print("Decrypted message:", decrypted_message)

else:
    # If an invalid mode is chosen, display an error message
    print("Invalid choice. Please enter 1 or 2.")
