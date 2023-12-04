latitude=float(input("Введіть широту: "))
longitude=float(input("Введіть довготу: "))

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def get_current_time(latitude, longitude):
    geolocator = Nominatim(user_agent="geo_app")
    location = geolocator.reverse((latitude, longitude), language='en')
    
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=longitude, lat=latitude)
    timezone = pytz.timezone(timezone_str)
    
    current_time = datetime.now(timezone)
    
    return location.address, current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

location, current_time = get_current_time(latitude, longitude)
print(f"Місце: {location}")
print(f"Поточний час: {current_time}")

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")