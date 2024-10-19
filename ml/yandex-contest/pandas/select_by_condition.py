# X. Самостоятельная 6.3. Выборка данных по условию
# Загрузите данные из файла revexp.csv (данные о доходах и расходах организаций) в dataframe df
# Выберите все данные за один год
# Выберите все доходы(revenue) = 0
# Выберите организации чьи расходы (expenditure) больше 8873000

import pandas as pd

import pandas as pd

df = pd.read_csv('revexp.csv', delimiter=';')
df.set_index('tin', inplace = True)

df_year = df[df['year'] == 2021]
print("Выборка данных только за 2021 год:\n", df_year.head())

df_revenue = df[df['revenue'] == 0]
print("\nВыборка всех нулевых доходов:\n", df_year.head())

df_expenditure = df[df['expenditure'] > 8873000]
print("\nВыборка расходов доходов более 887300:\n",df_expenditure)