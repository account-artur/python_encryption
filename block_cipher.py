text = "helloworld"
 
keys = {
    'a': '11', 'b': '12', 'c': '13', 'd': '14',
    'e': '15', 'f': '16', 'g': '21', 'h': '22',
    'i': '23', 'j': '24', 'k': '25', 'l': '26',
    'm': '31', 'n': '32', 'o': '33', 'p': '34',
    'q': '35', 'r': '36', 's': '41', 't': '42',
    'u': '43', 'v': '44', 'w': '45', 'x': '46',
    'y': '51', 'z': '52', '0': '53', '1': '54',
    '2': '55', '3': '56', '4': '61', '5': '62',
    '6': '63', '7': '64', '8': '65', '9': '66'
}
 
#encryption
crypt = ""
for i in text:
    if i in keys:
        crypt += keys[i]
        crypt += " "
print(crypt)
 
#decryption
temp = ""
decrypt = ""
for i in crypt:
    if i != " ":
        temp += i
    else:
        for j in keys:
            if keys[j] == temp:
                decrypt += j
        temp = ""
print(decrypt)