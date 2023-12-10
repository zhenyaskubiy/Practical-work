encryption_key = {
    'a': 'd', 'b': 'y', 'c': 'p', 'd': 'r', 'e': 'i', 'f': 'a', 'g': 'j', 'h': 'u', 'i': 'h',
    'j': 't', 'k': 'q', 'l': 'w', 'm': 'e', 'n': 's', 'o': 'f', 'p': 'o', 'q': 'v', 'r': 'c',
    's': 'n', 't': 'b', 'u': 'l', 'v': 'x', 'w': 'm', 'x': 'k', 'y': 'z', 'z': 'g'
}

def encrypt(text):
    encrypted_text = ''.join(encryption_key.get(c, c) for c in text.lower())
    return encrypted_text

def decrypt(encrypted_text):
    reversed_key = {v: k for k, v in encryption_key.items()}
    decrypted_text = ''.join(reversed_key.get(c, c) for c in encrypted_text)
    return decrypted_text

input_text = input("Введіть текст для шифрування: ")

encrypted_result = encrypt(input_text)
decrypted_result = decrypt(encrypted_result)
print("Шифрований текст:", encrypted_result)
print("Дешифрований текст:", decrypted_result)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")