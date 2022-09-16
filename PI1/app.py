import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/pregunta1")
def read_root():
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
    return f"El año con mas carreras es {año} y se corrieron {max(lista2)} carreras"



@app.get("/pregunta2")
def read_root():
    df = pd.read_json('Datasets\\results.json', lines=True)
    df = df[(df.position != r'\N')]
    df = df.reset_index()

    lista2 =[]


    contar =0
    df2 = df["position"].tolist()

    for i in df2:
        if i == 1:
            lista = df2.index(i)



            lista2.append(contar)
        contar= contar+1



    lista3=[]




    for j in lista2:
        posicion= df.iloc[j, 3]
        lista3.append(posicion)


    mylist = list(dict.fromkeys(lista3))
    lista4 =[]
    for k in mylist:

        
        df1= df[df["driverId"]==k].count()["driverId"]
        lista4.append(df1)
        


    lista4 = {i:lista3.count(i) for i in lista3}

    max_key = max(lista4, key=lista4.get)




    df = pd.read_json('Datasets\drivers.json', lines=True)

    driveridl = df["driverId"].tolist()
    drivername = df["driverRef"].tolist()





    for i in driveridl:
        if i == max_key:
            lista5 = df2.index(i)
        

    index = 0
    for i in drivername:
        if index==lista5:


            return f'El Piloto con mayor cantidad de primeros puestos es {i}'
            
        else:
            pass
        index = index + 1
        
@app.get("/pregunta3")
def read_root():
    df = pd.read_csv('Datasets/races.csv', encoding='utf8')

    df2= df.pivot_table(columns=['name'], aggfunc='size')

    max1 =max(df2)

    df2 = df2.to_dict()

    max_key = max(df2, key=df2.get)

    return f'El Nombre del circuito más corrido es: {max_key}'


@app.get("/pregunta4")
def read_root():
    df = pd.read_json('Datasets\\results.json', lines=True)

    df2 = pd.read_json('Datasets\constructors.json', lines=True)




    suma = df.groupby('constructorId')['points'].sum()

    df3 = pd.DataFrame(suma)


    df4 = df3.merge(df2, how='inner', on='constructorId')


    df6 = df4[df4["nationality"].str.contains("American|British")]



    puntos = df6['points'].max()

    df7 = df6.loc[df6['points'] == puntos]

    nombre = dict(df7['name'])



    return f'El Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British es: {nombre[0]}'

