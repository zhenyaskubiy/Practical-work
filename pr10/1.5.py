set1 = {3, 4, 5, 1, 2, 7, 8, 9}
elements_to_remove = {2, 9, 5}

set1.difference_update(elements_to_remove)

print("Оновлена множина:", set1)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")