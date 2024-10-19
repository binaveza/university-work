# O. Самостоятельная 2. Индексы в Pandas
# Создайте датасет movies с признаками ['id','movie','year','genre'], укажите в качестве индекса столбец с названием 'id'.
# Выведите список столбцов.

import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'movie': ['Trainspotting', 'The Full Monty', 'Skyfall', 'The Imitation Game', 'Pride & Prejudice'],
    'year': [1996, 1997, 2012, 2014, 2005],
    'genre': ['Drama', 'Comedy', 'Adventure', 'Biography', 'Romantic']
}

movies = pd.DataFrame(data)

# Устанавливаем 'id' как индекс
movies.set_index('id', inplace=True)

# Выводим список столбцов
print(movies.columns.tolist())
