# T. Самостоятельная 6.2. Выборка строк
# Загрузите данные из файла smb.csv в dataframe smb_df (обратите внимание на разделитель данных).
# Укажите в качестве индекса столбец с названием 'tin'.
# Выведите список столбцов.
# С помощью метода loc выберите строки c индексами [323389352, 323397610, 542002689] и столбец 'org_name'
# С помощью метода iloc выберите первые 30 строк и 2 по 4 столбцы

import pandas as pd

import pandas as pd

smb_df = pd.read_csv('smb.csv', delimiter=';')
smb_df.set_index('tin', inplace=True)

print("Список столбцов:", smb_df.columns.tolist())
print("Выборка с помощью loc:\n", smb_df.loc[[323389352, 323397610, 542002689], 'org_name'])
print("Выборка с помощью iloc:\n", smb_df.iloc[0:30, 1:4])