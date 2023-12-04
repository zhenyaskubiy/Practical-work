import calendar
def friday_13(month, year):
    day_of_week=calendar.weekday(year, month, 13)
    return day_of_week==calendar.FRIDAY
print(friday_13(3, 2020))  
print(friday_13(10, 2017))  
print(friday_13(1, 1985)) 

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")
