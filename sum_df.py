import pandas as pd
data = {'Name':['Tom', 'Jack', 'Jack','Cheo', 'Jack','Cheo'],'shop_code':[28,34,29,42,12,9],'Deuda':[180,224,139,972,87,23]}
df = pd.DataFrame(data)


#print(df)

#categories = df['Name'].unique()
#print("Lista de nombres: ", categories)

#Voy a pasar dos parámetros: df, column_name(La columna a la que quiero aplicar la categorización)
#El segundo parámetro Name se mete entre comillas.

def categorizer(df,column_name):
    categories = df[column_name].unique()
    dicts=[]
    i=0
    while i < len(categories):
        if categories[i]:
            print("hola", categories[i])
            print(df.Deuda.loc[df[column_name] == categories[i]].sum())
        #Esto es para agregar en una columna nueva
        #dicts.append("hola")
        i+=1

categorizer(df,'Name')




#print(dicts)

#print(df.Deuda.loc[df['Name'] == 'Tom'].sum())
#print(df.Deuda.loc[df['Name'] == 'Jack'].sum())

#print("Suma de Tom:", sumao.sum())
#print("Suma de Jack:", sumat.sum())


#axis =1 means across the column
#axis = 0 means across the rows
