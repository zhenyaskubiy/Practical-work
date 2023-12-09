my_dict = {
    'a': [27, 16, 43, 21],
    'b': [42, 19, 17, 82],
    'c': [52, 38, 20, 68]
}

sum_by_key = {key: sum(values) for key, values in my_dict.items()}

lists_by_column = list(zip(*my_dict.values()))

sum_by_column = [sum(column) for column in lists_by_column]

total_sum = sum(sum(values) for values in my_dict.values())

print("Суми елементів у списках за ключем:")
print(sum_by_key)

print("Суми елементів у списках по стовпчику:")
print(sum_by_column)

print("Загальна сума всіх елементів усіх списків:")
print(total_sum)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")