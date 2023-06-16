import pandas as pd

url = "https://raw.githubusercontent.com/AlanPerdomo/NF3-BIG-DATA-AlanPerdomo/main/1/world_alcohol.csv"
data = pd.read_csv(url,encoding='latin-1')

'''
# A) ----------------------------
print("Questao A:")
tipoBebidas = data.groupby("Beverage Types")
for tipo, grupo in tipoBebidas:
    print("Tipo de bebida:",tipo)
    print(grupo)
    print()

# B) ----------------------------
print("Questao B:")
anoRegiao = data.groupby(["WHO region", "Year"])
for (regiao, ano), grupo in anoRegiao:
    print("Região:", regiao)
    print("Ano:", ano)
    print(grupo)
    print()
'''
# C) ----------------------------
print("Questao C:")

contagemRegioes = data["WHO region"].value_counts()
print("Contagem de Regiões:")
print(contagemRegioes)
print()



contagemPaises = data["Country"].value_counts()
somaValoresPorBebidas = data.groupby("Beverage Types")["Display Value"].sum()
# D) ----------------------------
print("Questao D:")
statusValores = data.groupby("Beverage Types")["Display Value"].describe()
# E.1) ----------------------------
print("Questao E.I:")
bebidas1985 = data[data["Year"] == 1985]["Beverage Types"]
# E.2) ----------------------------
print("Questao E.II:")
regiao = data[data["Display Value"] > 4]["WHO region"]








