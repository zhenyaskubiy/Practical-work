import numpy as np
values = np.array([1, 2, 3, 4])

matrix = np.diag(values, k=-1)

print(matrix)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")