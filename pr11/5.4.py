import pandas as pd
input_series = pd.Series([7, 14, 21, 30, 35, 40])
positions = input_series[input_series % 7 == 0].index.tolist()
print("Позиції чисел, кратних 7:")
print(positions)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")