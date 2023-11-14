import math
katet1=int(input("Введіть довжину протилежного катета: "))
prot_kut=int(input("Введіть протилежний кут: "))
katet2=round(katet1/math.tan(prot_kut*3.1416/180))
print(f"Довжина прилеглого катета: ",katet2)
gip=round((katet1/math.sin(prot_kut*3.1416/180)))
print(f"Довжина гіпотенузи: ",gip)
perim=katet1+katet2+gip
print(f"Периметр: ",perim)
pril_kut=90-prot_kut
print(f"Прилеглий кут: ",pril_kut)
pperim=perim/2
area=round(math.sqrt(pperim*(pperim-katet1)*(pperim-katet2)*(pperim-gip)))
print(f"Площа: ",area)