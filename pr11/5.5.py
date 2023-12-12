import pandas as pd
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

positions = [2, 4, 6, 8]

print(s[positions])
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")