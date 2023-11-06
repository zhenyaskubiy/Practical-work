height_cm=int(input("Введіть зріст у см: "))
height_d=height_cm/2.54
height_f=int(height_d//12)
height_d=int(height_d%12)
print(f"Зріст у футах з дюймами: {height_f} фт і {height_d} дм")