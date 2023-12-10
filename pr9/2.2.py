import re

def reformat_date(date):

    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    
    reformatted_date = re.sub(pattern, r'\3-\2-\1', date)
    
    return reformatted_date

input_date = '2023-08-25'
output_date = reformat_date(input_date)
print("Вхідна дата:", input_date)
print("Результат перетворення:", output_date)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")