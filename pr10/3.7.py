import numpy as np

vector = np.random.rand(10)

print("Початковий вектор:")
print(vector)

max_value = np.max(vector)
max_index = np.argmax(vector)

print("Максимальне значення:", max_value)
print("Індекс максимального значення:", max_index)

vector[max_index] = 0

print("Вектор після заміни максимального значення на 0:")
print(vector)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")