from datetime import datetime
def strptime(date_str, date_format):

    d=datetime.strptime(date_str, date_format)
    return d.strftime("%Y%d%m") #%Y-рік (4 числа)
                                #%d-день місяця
                                #%m-номер місяця: 
date1="11/12/2023"
date2="12/31/2023"
date3="01/15/2022"                         
print(strptime(date1, "%m/%d/%Y")) 
print(strptime(date2, "%m/%d/%Y"))  
print(strptime(date3, "%m/%d/%Y")) 

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")