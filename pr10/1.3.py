set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

if set1.issubset(set2):
    print("set1 є підмножиною set2")
elif set2.issubset(set1):
    print("set2 є підмножиною set1")
else:
    print("Жодна з множин не є підмножиною одна одної")
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")