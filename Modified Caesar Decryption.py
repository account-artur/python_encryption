import random
key = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def encrypt(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) - n) % 33
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def decrypt(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) + n) % 33
            result += key[i]
        except ValueError:
            result += l
    return result
inkey = input("Enter a key: ")
intext = input("Enter a text: ")
text = intext
r = int(inkey)
shift = r                        
encrypted = encrypt(shift, text)
print('Зашифрованный текст:', text)
print('Расшифровал:', encrypted)
