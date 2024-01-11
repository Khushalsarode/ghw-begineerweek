def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Encrypt uppercase characters
            if char.isupper():
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

if __name__ == "__main__":
    # Example usage
    original_text = "Hello, Cryptology!"
    shift_value = 3

    encrypted_text = encrypt(original_text, shift_value)
    decrypted_text = decrypt(encrypted_text, shift_value)

    print("Original Text:", original_text)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
