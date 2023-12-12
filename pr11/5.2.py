# -*- coding: utf-8 -*-

import pandas as pd

# Список з ПІБ одногрупників
names = ['Іванов Іван', 'Петров Петро', 'Сидорова Марія']

# Створення датафрейму зі стовпцем ПІБ
df = pd.DataFrame(names, columns=['Full Name'])

# Розбиття стовпця ПІБ на ім'я та прізвище
df[['First Name', 'Last Name']] = df['Full Name'].str.split(' ', 1, expand=True)

# Виведення отриманого датафрейму
print(df)
