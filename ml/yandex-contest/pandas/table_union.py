# U. Самостоятельная 7. Объединение таблиц
# Создайте датафреймы из списков empoyees и empoyees_group.
# Для датасета с информацией о сотрудниках установите названия столбцов: ['Name', 'Age', 'City', 'Experience']
# Задайте ключи сотрудникам: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Для датасета с информацией об отделах сотрудников установите названия столбцов: ['index', 'Group']
# В качестве ключей установите столбец 'index'
# Объедините датасеты. Укажите метод outer для объединения.
# Заполните пропуски в столбце 'Group' значениями 'not_specified'

import numpy as np
import pandas as pd

empoyees = [
          ('Михаил', 34, 'Самара', 5) ,
          ('Роман', 31, 'Рязань' , 7) ,
          ('Анна', 16, np.nan, 11) ,
          ('Мария', 31,'Москва' , 7) ,
          ('Вероника', np.nan, 'Москва' , 4) ,
          ('Дмитрий', 35, 'Омск', 5 ),
          ('Шамиль', 35, 'Рязань', 11)
          ]

empoyees_group = [
                   ('a', 'Managment'),
                   ('b','It'),
                   ('d','It'),
                   ('c','Administration'),
                   ('f','Administration')]

df_employees = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Experience'])
df_employees['Key'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

df_empoyees_group = pd.DataFrame(empoyees_group, columns=['index', 'Group']).set_index('index')

df_full = pd.concat([df_employees, df_empoyees_group], axis=1, join='outer')
print("Общий датасэт:\n", df_full)

#df_full['Group'] = df_full['Group'].fillna('not_specified', inplace=True)
#df_full = df_full.where(pd.notnull(df_full), 'not_specified')
df_full['Group'] = df_full['Group'].where(df_full['Group'].notnull(), 'not_specified')
print("\nОбщий датасэт без пропусков:\n", df_full)


