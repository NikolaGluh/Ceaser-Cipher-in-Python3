#A python program for Caesar Cipher

# Main function for user input and printing results
def main():
    while True:
        text = input("Enter your text: ")
        choice = input("Do you want to encrypt or decrypt text? (encrypt/decrypt): ").strip().lower()

        if choice == "encrypt" or choice == "e":
            try:
                s = int(input("How many shifts would you like? "))
            except ValueError:
                print("Please enter a valid number for shifts.")
                continue
            
            print(f"\nText: {text}
                    \nShift: {s}
                    \nCipher: {cipher(text, s, direction=1)}")
        elif choice == "decrypt" or choice == "d":
            print("\nCipher: " + text)
            print("Results:")
            for i in range(26):
                print(f"Shift {i}: {cipher(text, i, direction=-1)}")

        else:
            print("Please enter 'encrypt' or 'decrypt'.")
            continue

        input('\nPress any key to exit.')
        break

# Function for shifting letters backwards or forwards
def cipher(text, s, direction=1):
    result = ""

    for char in text:
        if char.isupper():
            # 65 is ASCII decimal for uppercase 'A'
            result += chr((ord(char) - 65 + direction * s) % 26 + 65)
        elif char.islower():
            # 97 is ASCII decimal for lowercase 'a'
            result += chr((ord(char) - 97 + direction * s) % 26 + 97)
        else: # Keep the character if it's a special character (like Space)
            result += char

    return result

# Calling main function once
main()
