#Encryption / Decryption program

import random,string,time

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
print(f"CHARS : {chars}")
key = chars.copy()
random.shuffle(key)
print(f"KEYS : {key}")

#ENCRYPTION
plain_text = input("ENTER THE MESSAGE TO ENCRYPT: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index ]

print(f"PLAIN MESSAGE : {plain_text} ")
print(f"ENCRYPTED MESSAGE : {cipher_text} ")


time.sleep(1)


#DECRYPTION

cipher_text = input("ENTER THE MESSAGE TO DECRYPT: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index ]

print(f"ENCRYPTED MESSAGE : {cipher_text}")
print(f"PLAIN MESSAGE : {plain_text}")