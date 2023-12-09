import numpy as np

matrix1 = np.random.random((5, 3))
matrix2 = np.random.random((3, 2))

print("Матриця №1:")
print(matrix1)
print("Матриця №2:")
print(matrix2)

result_dot = np.dot(matrix1, matrix2)
result_matmul = np.matmul(matrix1, matrix2)
result_at = matrix1 @ matrix2

print("Результат з використанням numpy.dot():")
print(result_dot)

print("Результат з використанням numpy.matmul():")
print(result_matmul)

print("Результат з використанням оператора @:")
print(result_at)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")