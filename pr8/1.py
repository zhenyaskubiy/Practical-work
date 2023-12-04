from datetime import datetime, timedelta
def game_release(year, month):
    first_day_of_month=datetime(year, month, 1)
    day_of_week=first_day_of_month.weekday()
    days_to_thursday=(3-day_of_week+7)%7
    first_thursday=first_day_of_month+timedelta(days=days_to_thursday)
    return first_thursday.strftime("%Y-%m-%d")
print(game_release(2024, 1))
print(game_release(2021, 2))

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")