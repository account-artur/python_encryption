def encrypt(text,s): 
    result = "" 
  
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
    return result 

TEXT = "ABCDEFG"
SHIFT = 4
print("Text  : " + TEXT )
print("Shift : " + str(SHIFT))
print("Cipher: " + encrypt(TEXT,SHIFT))