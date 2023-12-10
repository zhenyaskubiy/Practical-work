text = input("Введіть текст: ")

word= len(text.split())
letter= sum(c.isalpha() for c in text)
digit= sum(c.isdigit() for c in text)
lowercase= sum(c.islower() for c in text)
uppercase= sum(c.isupper() for c in text)
space= sum(c.isspace() for c in text)

print(f"Кількість слів: {word}")
print(f"Кількість букв: {letter}")
print(f"Кількість цифр: {digit}")
print(f"Кількість малих літер: {lowercase}")
print(f"Кількість великих літер: {uppercase}")
print(f"Кількість пробілів: {space}")
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")