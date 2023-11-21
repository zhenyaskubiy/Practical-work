luna_dig=0
s_luna=0

imei=input("Введіть IMEI: ")
for i in range(len(imei)):
     dig=int(imei[i])
     if i%2==0:
        s_luna+=dig
     else:
        doubled=dig*2
        s_luna+=doubled if doubled<10 else doubled-9
luna_dig=s_luna%10 if s_luna%10==0 else 10-(s_luna%10)
if luna_dig==6:
    print("Цифра Луна відповідає виробнику.")
else:
    print("Цифра Луна не відповідає виробнику.")