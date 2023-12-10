x = 2
y = 3
z = x ** y

print(f"{x} у степені {y} буде дорівнювати {z}.")

sliced_string = "у степені " + str(y)

reversed_string = sliced_string[::-1]

print(reversed_string)


import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")