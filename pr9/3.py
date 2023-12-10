import re

def find_word_indices(word, text):
    matches = re.finditer(r"\b" + re.escape(word) + r"\b", text)
    for match in matches:
        start_index = match.start()
        end_index = match.end()
        print(f"Match '{word}' found: Start Index - {start_index}, End Index - {end_index}")

text = "Я люблю місто Черкаси, це місто неймовірне"

word_to_find = "місто"

find_word_indices(word_to_find, text)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")