def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
original_text = "Hello, World!"
encrypted_text = rot13(original_text)
decrypted_text = rot13(encrypted_text)

print("Original Text:", original_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
