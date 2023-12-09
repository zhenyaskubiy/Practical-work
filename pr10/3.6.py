import numpy as np
vector = np.linspace(0, 1, num=10, endpoint=False)[1:]  

print(vector)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")