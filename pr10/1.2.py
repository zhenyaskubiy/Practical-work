list1 = ['hello', 'world', 'Python', 'C', 'Java', 'Python']
list2 = ['Python', 'Java', 'PHP', 'HTML', 'Java', 'PHP']
set1 = set(list1)
set2 = set(list2)

result = set1 - set2

print("Слова, що присутні в списку 1, але відсутні в списку 2:")
print(list(result))
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")