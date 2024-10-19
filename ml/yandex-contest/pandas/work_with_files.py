# Q. Самостоятельная 4. Сохранение/Выгрузка данных в файл/из файла
# Загрузите данные из файла movies_small.csv в dataframe my_movies, укажите в качестве индекса столбец с названием 'ID'

import pandas as pd
filepath = "movies_small_df.csv"
movies = pd.read_csv(filepath,index_col='ID')
