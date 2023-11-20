tarif=input("Оберіть тариф (1000/2000/5000): ")
mb=int(input("Введіть кількість витрачених мегабайтів: "))
if tarif=="1000":
    price=20
    plusprice=0.05
    megabites=1000
    print(f"Якби Ви перейшли на тариф 2000, віртість за місяць становила б 35 грн")
    print(f"Якби Ви перейшли на тариф 5000, віртість за місяць становила б 85 грн")
elif tarif=="2000":
    price=35
    plusprice=0.04
    megabites=2000
    print(f"Якби Ви перейшли на тариф 5000, віртість становила б 85 грн")
elif tarif=="5000":
    price=85
    plusprice=0.02
    megabites=5000
if mb<=megabites:
    total=price
else:
    plusmb=mb-megabites
    total=price+(plusmb*plusprice)
print(f"Підсумковий рахунок за місяць становить {total} грн")