import pandas as pd

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([3, 4, 5, 6, 7])

# Виведення елементів, які не є спільними для обох серій
not_common_elements = pd.concat([series1[~series1.isin(series2)], series2[~series2.isin(series1)]])
print("Елементи, які не є спільними для двох серій:")
print(not_common_elements)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")