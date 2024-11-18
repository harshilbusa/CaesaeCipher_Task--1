# Function to encrypt the message
def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

# Function to decrypt the message
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main Program
if __name__ == "__main__":
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    choice = input("Encrypt or Decrypt? (E/D): ").upper()

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter E for Encrypt or D for Decrypt.")
