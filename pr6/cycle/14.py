loan=20000
m_loan=0.015
m_pay=1000
months=0 
while loan>0:
    perc=loan*m_pay
    loan=loan+perc-m_pay
    months+=1
    if loan<m_pay:
        months+=1
        break
 
   
print(f"Кількість місяців для погашення кредиту: {months}")