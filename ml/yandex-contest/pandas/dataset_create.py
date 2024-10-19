# N. Самостоятельная 1. Создание датасета
# Создайте датасет домашних животных КотоКафе с колонками: Кличка, Год Рождения, Пол, Цвет, Порода.
# (имена колонок указывайте на английском: Name, YearBirth, Gender, Color, Breed)
#
# Создайте одномерный набор данных о темпераменте кошек - Temperament

import pandas as pd

data_dict = {
    'Name': ['Whiskers', 'Muffin', 'Shadow', 'Pudding', 'Tigger'],
    'YearBirth': [2019, 2020, 2021, 2022, 2023],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male'],
    'Color': ['White', 'Black', 'Gray', 'Ginger', 'Tabby'],
    'Breed': ['Maine Coon', 'Siamese', 'Persian', 'Ragdoll', 'Bengal']
}

df = pd.DataFrame(data_dict)

print("Cat Cafe:")
print(df)

temperament_data = ['Affectionate', 'Independent', 'Energetic', 'Calm', 'Social', 'Vocal']
temperament_series = pd.Series(temperament_data, name='Temperament')

print("\nCat temperament:")
print(temperament_series)
