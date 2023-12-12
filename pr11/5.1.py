import pandas as pd
import numpy as np

# Створення датафрейму з випадковими даними
data = {
    'A': [1, 2, 8, 4],
    'B': [5, 5, np.nan, 8],
    'C': [8, 10, 11, 12]
}
df = pd.DataFrame(data)

# Обчислення відсотка відсутніх записів у кожному стовпці
missing= (df.isnull().sum() / len(df)) * 100
print("Відсоток відсутніх записів у кожному стовпці:")
print(missing)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")