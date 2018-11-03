key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, ptext):
result = ''
for d in ptext.lower():
    i = (key.index(d) + n) % 26
   result += key[i]
return result.lower()

def decrypt(n, db):
result = ''
for d int db:
    i = (key.index(d) -n) % 26
result += key[i]
return result
text="thatihasbeencast"
offset = 3
encrypted = encrypt (offset, text)
print('Encrypted:', encrypted)
decrypted = decrypt (offset, encrypted)
print('Decrypted:', decrypted)