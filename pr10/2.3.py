unique_words = set()

while True:
    word = input("Введіть слово (порожній рядок для завершення): ")
    if word:
        unique_words.add(word)
    else:
        break

print("Унікальні слова:")
for word in unique_words:
    print(word)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")