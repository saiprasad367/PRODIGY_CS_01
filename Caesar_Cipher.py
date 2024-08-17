def encrypt(Text, shift):
    encrypted_Text = ""
    for char in Text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_Text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_Text += char
    return encrypted_Text

def decrypt(Text, shift):
    decrypted_Text = ""
    for char in Text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_Text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_Text += char
    return decrypted_Text

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for encrypt or 'D' for decrypt.")
        return

    Text = input("Enter the Text: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if choice == 'E':
        result = encrypt(Text, shift)
        print("Encrypted Text:", result)
    else:
        result = decrypt(Text, shift)
        print("Decrypted Text:", result)

if __name__ == "__main__":
    main()
