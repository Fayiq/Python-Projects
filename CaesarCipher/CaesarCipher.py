def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            encrypted += c
    return encrypted

def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            decrypted += c
    return decrypted

print("CAESAR CIPHER: \n")
option = int(input("1: Encrypt text\n2: Decrypt text\nENTER THE OPTION: "))

if(option==1):
    plain_text = str(input('Enter the string to encrypt: '))
    key = int(input("Enter the shift for the encryption: "))
    print("The encrypted text is: ",cipher_encrypt(plain_text,key))
elif(option==2):
    cipher_text = str(input("Enter the string to decrypt: "))
    key = int(input("Enter the key for decryption: "))
    print("The decrypted text is: ",cipher_decrypt(cipher_text,key))
else:
    print("Enter proper option")