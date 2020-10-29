TEXT = input()

a = (TEXT[4::5])
b = (TEXT[3::5])
c = (TEXT[2::5])
d = (TEXT[1::5])
f = (TEXT[::5])

print("ENCRYPTED:")
print(a+b+c+d+f)
print("DECRYPTED:")
print(TEXT)