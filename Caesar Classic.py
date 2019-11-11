key = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def encrypt(n, plaintext):
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 33
            if i < 33:
                i-33
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def decrypt(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 33
             if i < 33:
                i+33
            result += key[i]
        except ValueError:
            result += l
    return result

text = "С 1 января 2020 года в Казахстане запускается система обязательного социального медицинского страхования.  Хочу донести до каждого – государство сохраняет гарантированный объём бесплатной медицинской помощи. На его финансирование будет направлено более 2,8 трлн тенге в течение следующих трёх лет. Обязательное социальное медстрахование признано улучшить качество и доступность медуслуг. В рамках трёхлетнего бюджета будет направлено дополнительно 2,3 трлн тенге на развитие системы здравоохранения. Правительству нужно предельно ответственно подойти к вопросу реализации социального медстрахования во избежание его очередной дискредитации. Права на ошибку у нас уже нет."
s = ("ключдляшифрования")
print("Initial key is:")
print (s)
first=[c for c in s]  
second=[ord(c) -1071 for c in s]
print("Number key is:")
for second in second :print(second, end = '')
shift = second                        
print("")
encrypted = encrypt(shift, text)
print('Encrypted:', encrypted)
decrypted = decrypt(shift, encrypted)
print('Decrypted:', decrypted)
