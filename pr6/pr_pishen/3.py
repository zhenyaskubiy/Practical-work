T=float(input("Введіть температуру в градусах Цельсія: "))
V=float(input("Введіть швидкість вітру в км/год: "))
wci = float(round(13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16))
if T<10 and V>4.8:
    print(f"Індекс прохолодності вітру: ", wci)
else :
    print(f"Індекс прохолодності вітру не коректний")