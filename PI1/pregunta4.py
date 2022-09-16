import pandas as pd


#- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British



df = pd.read_json('Datasets\\results.json', lines=True)

df2 = pd.read_json('Datasets\constructors.json', lines=True)




suma = df.groupby('constructorId')['points'].sum()

df3 = pd.DataFrame(suma)


df4 = df3.merge(df2, how='inner', on='constructorId')


df6 = df4[df4["nationality"].str.contains("American|British")]



puntos = df6['points'].max()

df7 = df6.loc[df6['points'] == puntos]

nombre = dict(df7['name'])



print(f'El Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British es: {nombre[0]}')

