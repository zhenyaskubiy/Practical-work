def remove_zeros(ip):
    parts=ip.split('.')

    parts= [str(int(part)) for part in parts]
    

    return '.'.join(parts)
ip_address='192.168.001.02'

result = remove_zeros(ip_address)
print("Оригінальна IP-адреса:", ip_address)
print("IP-адреса без нулів:", result)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")