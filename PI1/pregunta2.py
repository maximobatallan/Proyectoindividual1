import pandas as pd

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


        print(f'El Piloto con mayor cantidad de primeros puestos es {i}')
        
    else:
        pass
    index = index + 1
