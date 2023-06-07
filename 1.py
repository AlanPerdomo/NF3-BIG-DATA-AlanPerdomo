import pandas as pd

data = pd.read_csv('world_alcohol.csv')
tipoBebidas = data.groupby('Beverage Types')
anoRegiao = data.groupby(['WHO region','Year'])

#print(data)
print(anoRegiao.head())



# 
# # a. Agrupar os dados por tipo de bebidas
# grouped_by_beverage = data.groupby('Beverage')
# 
# # b. Agrupar os dados por Região e por Ano
# grouped_by_region_year = data.groupby(['Region', 'Year'])
# 
# # c. Seção de Contagens
# region_counts = data['Region'].value_counts()
# country_counts = data['Country'].value_counts()
# beverage_sum = data.groupby('Beverage')['Value'].sum()
# 
# # d. Análises estatísticas da coluna dos valores
# value_stats = data.groupby('Beverage')['Value'].describe()
# 
# # e. Resultados de acordo com critérios
# # i. Mostrar a coluna de bebidas do ano de 1985
# beverages_1985 = data[data['Year'] == 1985]['Beverage']
# 
# # ii. Mostrar a coluna de Região com valores acima de 4
# regions_above_4 = data[data['Value'] > 4]['Region']
# 
# # Exibir os resultados
# print("Agrupados por tipo de bebida:")
# print(grouped_by_beverage.head())
# print("\nAgrupados por Região e por Ano:")
# print(grouped_by_region_year.head())
# print("\nContagem de Regiões:")
# print(region_counts)
# print("\nContagem de Países:")
# print(country_counts)
# print("\nSoma da coluna de valores por Bebida:")
# print(beverage_sum)
# print("\nEstatísticas da coluna dos valores:")
# print(value_stats)
# print("\nColuna de bebidas do ano de 1985:")
# print(beverages_1985)
# print("\nColuna de Região com valores acima de 4:")
# print(regions_above_4)
# 