import pandas as pd

data = pd.read_csv('world_alcohol.csv')

# A)
tipoBebidas = data.groupby('Beverage Types')['Beverage Types'].count()
# B)
anoRegiao = data.groupby(['WHO region','Year'])
# C)
contagemRegioes = data['WHO region'].value_counts()
contagemPaises = data['Country'].value_counts()
somaValoresPorBebidas = data.groupby('Beverage Types')['Display Value'].sum()
# D)
statusValores = data.groupby('Beverage Types')['Display Value'].describe()
# E.1)
bebidas1985 = data[data['Year'] == 1985]['Beverage Types'] 
# E.2)
regiao=data[data['Display Value']>4]['WHO region'] 


print('Dados agrupados por tipo de bebidas: \n', tipoBebidas)








