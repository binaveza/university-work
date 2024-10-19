# R. Самостоятельная 5. Встроенные методы анализа и обработки данных
# Загрузите данные из файла books_part1.csv в dataframe books
# Выведите размерность данных
# Выведите список столбцов
# Выведите первые несколько строк
# Выведите список уникальных издателей и количество книг для каждой книги
# В переменную books_numbers сохраните только числовые признаки
# Выведите основные показатели статистики (min, max, mean и тд) для датасета books_numbers


import pandas as pd

books = pd.read_csv("books_part1.csv")

print("Размерность данных:", books.shape)
print("Список столбцов:", books.columns.tolist())
print("Первые несколько строк:\n", books.head())

publishers_info = books['Publisher'].value_counts()
print("Количество книг для каждого издателя:\n", publishers_info)

books_numbers = books.select_dtypes(include='number')
print("Только числовые признаки:\n", books_numbers)

statistics = books_numbers.describe()
print("Основные показатели статистики:\n", statistics)
