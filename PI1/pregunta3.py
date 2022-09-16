import pandas as pd

df = pd.read_csv('Datasets/races.csv', encoding='utf8')

df2= df.pivot_table(columns=['name'], aggfunc='size')

max1 =max(df2)

df2 = df2.to_dict()

max_key = max(df2, key=df2.get)

print(f'El Nombre del circuito más corrido es: {max_key}')