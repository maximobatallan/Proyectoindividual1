import pandas as pd


df = pd.read_csv('Datasets/races.csv', encoding='utf8')


df2 = df.drop_duplicates(subset=['year'])
df2 = df2["year"].tolist()

lista2 =[]
df1=0
conteo = 1



for lista in df2:

    
    df1= df[df["year"]==lista].count()["year"]
    lista2.append(df1)
    
    if df1 > conteo:
        conteo = df1
        año = lista





print(f"El año con mas carreras es {año} y se corrieron {max(lista2)} carreras")
