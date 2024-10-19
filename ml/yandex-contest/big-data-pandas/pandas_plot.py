# V. Самостоятельная 8. Графики в Pandas
# Выполните предварительный анализ данных для таблицы revexp.csv:
#
# Постройте график распределения данных
# Постройте график распределения дохода по годам

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('revexp.csv', delimiter=';')
#print(df.head())

df.hist()
#df.hist(column=None, by=None, bins=50, color='red')
#plt.suptitle('Data Distribution Plot')
plt.show()

grouped = df.groupby('year')['revenue'].sum().reset_index()
plt.bar(grouped['year'].astype(str), grouped['revenue'], color='#7409AA')
plt.xlabel('Год')
plt.ylabel('Общий доход')
plt.title('Распределение дохода по годам')
plt.show()