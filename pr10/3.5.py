import numpy as np

start_date = np.datetime64('2022-01-01')
end_date = np.datetime64('2022-02-01')

dates = np.arange(start_date, end_date, dtype='datetime64[D]')

print(dates)
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")