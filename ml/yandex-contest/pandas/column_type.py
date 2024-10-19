# P. Самостоятельная 3. Тип данных в столбцах
# Создайте DataFrame со столбцами: 'team' (строка), 'points' (целые числа),'rebounds'(целые числа),'blocks(целые числа).
# Заполните данными.
# Выберите столбцы с типом 'object'.

import pandas as pd

data = {
    'team': ['Team A', 'Team B', 'Team C'],
    'points': [90, 100, 110],
    'rebounds': [20, 30, 40],
    'blocks': [5, 6, 7]
}

df = pd.DataFrame(data)

print(df)

print("\nСтолбцы с типом 'object':")
print(df.select_dtypes(['object']))