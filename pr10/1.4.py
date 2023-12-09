set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.update(set2 - set1)

print("Оновлена перша множина:", set1)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")