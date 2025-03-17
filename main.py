def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
    
def vigenere_encrypt(text, key):
    encrypted = ""
    key_index = 0
    for char in text:
        if char.isalpha():  
            shift = ord(key[key_index % len(key)].lower()) - 97
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            encrypted += char  
    return encrypted

def vigenere_decrypt(text, key):
    decrypted = ""
    key_index = 0
    for char in text:
        if char.isalpha(): 
            shift = ord(key[key_index % len(key)].lower()) - 97
            shift_base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            key_index += 1
        else:
            decrypted += char 
    return decrypted
def main():
    print("Select an encryption method:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        text = input("Enter text to encrypt/decrypt: ")
        shift = int(input("Enter shift value for Caesar Cipher: "))
        
        encrypt_decrypt_choice = input("Encrypt (E) or Decrypt (D)? ").upper()
        
        if encrypt_decrypt_choice == 'E':
            print("Encrypted message: ", caesar_encrypt(text, shift))
        elif encrypt_decrypt_choice == 'D':
            print("Decrypted message: ", caesar_decrypt(text, shift))
        else:
            print("Invalid choice.")
    
    elif choice == '2':
        text = input("Enter text to encrypt/decrypt: ")
        key = input("Enter key for Vigenère Cipher: ")
        
        encrypt_decrypt_choice = input("Encrypt (E) or Decrypt (D)? ").upper()
        
        if encrypt_decrypt_choice == 'E':
            print("Encrypted message: ", vigenere_encrypt(text, key))
        elif encrypt_decrypt_choice == 'D':
            print("Decrypted message: ", vigenere_decrypt(text, key))
        else:
            print("Invalid choice.")
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
    
