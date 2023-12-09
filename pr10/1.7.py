my_dict = {
    'id1': {'name': 'Bob', 'area': 'IT'},
    'id2': {'name': 'Bob', 'area': 'IT'},
    'id3': {'name': 'Rob', 'area': 'Healthcare'},
    'id4': {'name': 'Julie', 'area': 'Marketing'}
}
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print("Словник без дублікатів значень:")
print(unique_dict)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")