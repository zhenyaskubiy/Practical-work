pressure=float(input("Введіть тиск у кПа: "))
pr_ppd=pressure*0.14503773773375
pr_mmhg=pressure*7.50062
pr_atm=pressure*0.00986923267
print(f"Еквівалентний тикс у фт/дм^2: {pr_ppd}")
print(f"Еквівалентний тикс у мм рт. ст.: {pr_mmhg}")
print(f"Еквівалентний тикс у атмосферах: {pr_atm}")