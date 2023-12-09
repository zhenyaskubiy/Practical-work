import numpy as np

arr = np.array([7,85,36,1000,18989798,845], dtype=np.int32)


bytes_count = arr.itemsize * arr.size
print("Кількість байтів, яку займає масив:", bytes_count)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")