m_voda=float(input("Введіть масу води в грамах: "))
delta_T=float(input("Введіть температурну зміну в градусах Цельсія: "))
pitoma_v=4.186
q=m_voda*delta_T*pitoma_v
print(f"Загальна кількість енергії: {q} Дж")
kwatgod=q/3600000
vart=1.33*kwatgod
print(f"Для нагріву 1 чашки води, що містить {m_voda} г, потрібно витратити {vart} грн")