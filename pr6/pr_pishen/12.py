import sys
vik=int(input("Введіть свій вік: "))
if vik<19:
    print("Калькулятор призначений для людей старших за 19 років.")
    sys.exit()
masa=float(input("Введіть масу тіла: "))
zrist=float(input("Введіть зріст: "))
system=input("Оберіть систему одиниць вимірювання (metr/dmft): ")
if system == "metr":
    imt=masa/zrist**2
elif system =="dmft":
    imt=703*masa/zrist**2
print(f"Ваш ІМТ: ", imt)
gen=input("Введіть Вашу стать (male/female): ")
if gen=="male":
    if imt<20:
        print("Ваш діагноз: нестача маси")
    elif imt>20 and imt<25:
        print("У Вас нормальна маса")
    elif imt>26 and imt<30:
        print("Ваш діагноз: надмірна маса")
    elif imt>31 and imt<40:
        print("Ваш діагноз: ожиріння")
    else: print("Ваш діагноз: тяжке ожиріння")
elif gen=="female":
    if imt<19:
        print("Ваш діагноз: нестача маси")
    elif imt>19 and imt<24:
        print("У Вас нормальна маса")
    elif imt>25 and imt<30:
        print("Ваш діагноз: надмірна маса")
    elif imt>31 and imt<40:
        print("Ваш діагноз: ожиріння")
    else: print("Ваш діагноз: тяжке ожиріння")


