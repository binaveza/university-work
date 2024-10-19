# S. Самостоятельная 6.1. Выборка столбцов
# Загрузите данные из файла smb.csv в dataframe smb_df (обратите внимание на разделитель данных).
# Укажите в качестве индекса столбец с названием 'tin'.
# Выведите список столбцов.
# С помощью метода loc выберите столбец 'org_name'
# Удалите индексы из таблицы
# С помощью оператора [] выберите столбец 'tin', 'org_name', 'region'

import pandas as pd

smb_df = pd.read_csv('smb.csv', delimiter=';')

#print(smb_df.columns)
columns = smb_df[['tin', 'org_name', 'region']]
print("Список выбранных столбцов: ", columns)

smb_df.set_index('tin', inplace=True)

print("Список столбцов:",smb_df.columns.tolist())

org_name = smb_df.loc[:, 'org_name']
print("Столбец org_name:\n", org_name)

smb_df = smb_df.reset_index(drop=True)
print("Без индексов:\n", smb_df.head())

