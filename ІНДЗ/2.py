from datetime import datetime
import pyttsx3

def speak_time(time_str):
    hours, minutes = map(int, time_str.split(':'))

    civil_time = datetime.strptime(time_str, '%H:%M').strftime('%I:%M %p')
    military_time = datetime.strptime(time_str, '%H:%M').strftime('%H:%M')    

    engine = pyttsx3.init()
    engine.say(f"Civilian time is {civil_time}")
    engine.say(f"Military time is {military_time}")
    engine.runAndWait()

time_input = "21:00" 
speak_time(time_input)
