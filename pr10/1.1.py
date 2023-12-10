def insertion_sort(arr):
  # Перебираємо елементи починаючи з індексу 1
    for i in range(1, len(arr)):
        key=arr[i] # Запам'ятовуємо поточний елемент
        j=i-1
# Порівнюємо key з попередніми елементами та зсуваємо їх
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = key  
nums=[18, 11, -56, 5, -5]
print("Початковий масив:", nums)

insertion_sort(nums)
print("Відсортований масив:", nums)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")