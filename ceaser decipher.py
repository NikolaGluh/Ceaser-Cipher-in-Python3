#A python program to illustrate Caesar Cipher Technique, modified by nik
#Original: https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
def main():
    text = input("Enter your text: ")
    choice = input("Do you want to encrypt or decrypt text? (ecrypt/decrypt): ")
    if choice.lower() == "encrypt":
        s = input("How many shifts would you like? ")
        print("Text : " + text)
        print("Shift : " + str(s))
        print("Cipher: " + encrypt(text,int(s)))
        input('\n Press any key to exit')
    elif choice.lower() == "decrypt":
        print("Cipher : " + text)
        print("Results: \n")
        for i in range(26):
            print(decrypt(text, i))
        input('\nPress any key to exit')
    else:
        input("Please enter a valid value.\n")
        main()

def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result
	result = ""

def decrypt(text, s):
	result = ""
	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) - s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) - s - 97) % 26 + 97)

	return result
	result = ""

#check the above function
main()
