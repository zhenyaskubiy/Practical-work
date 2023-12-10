import re

text = "Напишіть програму, яка виведе всі 6-символьні слова з тексту з використанням регулярного виразу. "

for match in re.finditer(r"\b\w{6}\b", text): 
    #\b- границяя слова
    #\w- будь-який символ буква чи цифра чи підкреслення
    #{6}- попередній символ \w має зустрітися 6 разів
    print(match.group())

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")