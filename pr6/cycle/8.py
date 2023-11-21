students=0
s_pr=0
s_ekz=0
while True:
    pr=float(input("Введіть оцінку за практичні: "))
    students+=1
    if pr==-1:
        break
    ekz=float(input("Введіть оцінку за екзамен: "))
    if pr>=5 and ekz>=5:
        total=pr*0.3+ekz*0.7
    else: 
        total=min(pr, ekz)
    print(f"Остаточна оцінка: {total}")
    s_pr=s_pr+pr
    s_ekz=s_ekz+ekz
    average_pr=s_pr/students
    average_ekz=s_ekz/students
    print(f"Середня оцінка по групі за практичні заняття: {average_pr}")
    print(f"Середня оцінка по групі за екзамени: {average_ekz}")