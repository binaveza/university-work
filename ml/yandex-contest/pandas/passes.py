# W. Самостоятельная 9. Работа с пропусками
# Выгрузите данные из файла 'tech-stocks.csv'.
#
# Заполните пропуски для числовых значений медианной, для строковых - значением 'other'.
# Удалите строки где все значения пропущены.
# Удалите столбцы где все значения пропущены.

import pandas as pd

df = pd.read_csv('tech-stocks.csv', delimiter=',')

print("\nНачальный датасэт:\n", df)

df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

print("\nДатасэт после удаления пустых строк и столбцов:\n", df)

df.fillna(df.median(numeric_only=True), inplace=True)
df.fillna('other', inplace=True)

print("\nДатасэт после заполнения пустых значений:\n", df)