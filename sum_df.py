import pandas as pd
data = {'Name':['Tom', 'Jack', 'Jack','Cheo', 'Jack','Cheo'],'shop_code':[28,34,29,42,12,9],'Deuda':[180,23,139,972,87,23], 'Tipo':[3,4,4,4,4,3]}
df = pd.DataFrame(data)


print("Data Frame: \n",df)

#categories = df['Name'].unique()
#print("Lista de nombres: ", categories)

#Voy a pasar dos parámetros: df, column_name(La columna a la que quiero aplicar la categorización)
#El segundo parámetro Name se mete entre comillas.

#ESTO SE HACE CON UNA TABLA MAS GENERAL (QUE TENGA LOS PRECIOS POR PACIENTE...???)
def categorizer(df,column_name):
    categories = df[column_name].unique()
    dicts=[]
    i=0
    print("**** Cuando es de Tipo 4 ***")
    while i < len(categories):
        if categories[i]:
            print("hola", categories[i])
            print((df.Deuda.loc[(df[column_name] == categories[i]) & (df['Tipo'] == 4)]))
            #ESTO ES DAME EL PRECIO DE PERSONA 1 EN TIPO 3 Ó CONSULTA ESPECIALISTA
            print((df.Deuda.loc[(df[column_name] == categories[i]) & (df['Tipo'] == 4)].sum()))
            #resulr.append() <- algo así
        i+=1

categorizer(df,'Name')



##CON GROUP BY ##

#categories = df['Name'].unique()
#i=0
#while i < len(categories):
#    if categories[i]:
#        df.groupby(categories[i], df['Tipo'] == 4)['Deuda'].agg('sum')
        #print(df.groupby([categories[i],df['Tipo'] == 4])['Number'].agg('sum')
#    i+=1

df.groupby(df['Name'].unique(), df['Tipo'] == 4)['Deuda'].agg('sum')



#print(dicts)

#print(df.Deuda.loc[df['Name'] == 'Tom'].sum())
#print(df.Deuda.loc[df['Name'] == 'Jack'].sum())

#print("Suma de Tom:", sumao.sum())
#print("Suma de Jack:", sumat.sum())


#axis =1 means across the column
#axis = 0 means across the rows
