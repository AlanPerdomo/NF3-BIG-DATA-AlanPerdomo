import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/AlanPerdomo/NF3-BIG-DATA-AlanPerdomo/main/1/world_alcohol.csv"
data = pd.read_csv(url, encoding="latin-1")

# A) ----------------------------
print("\nQuestao A:")
tipoBebidas = data.groupby("Beverage Types")
for tipo, grupo in tipoBebidas:
    print("Tipo de bebida:", tipo)
    print(grupo)
    print()

# B) ----------------------------
print("\nQuestao B:")
anoRegiao = data.groupby(["WHO region", "Year"])
for (regiao, ano), grupo in anoRegiao:
    print("Região:", regiao)
    print("Ano:", ano)
    print(grupo)
    print()

# C) ----------------------------
print("\nQuestao C:")

contagemRegioes = data["WHO region"].value_counts()
print("\nContagem de Regiões:\n", contagemRegioes)

contagemPaises = data["Country"].value_counts()
print("\nContagem de Países:\n", contagemPaises)

somaValoresPorBebidas = data.groupby("Beverage Types")["Display Value"].sum()
print("\nSoma da coluna de valores por Bebida:\n", somaValoresPorBebidas)

# D) ----------------------------
print("\nQuestao D:")

media = data["Display Value"].mean()
moda = data["Display Value"].mode().values[0]
mediana = data["Display Value"].median()
descritiva = data["Display Value"].describe()

print("Análises Estatísticas dos Valores:")
print("Média:", media)
print("Moda:", moda)
print("Mediana:", mediana)
print("Estatística Descritiva:")
print(descritiva)
print()

somaValoresPorBebidas.plot(kind="bar", rot=0)
plt.xlabel("Tipo de Bebida")
plt.ylabel("Soma dos Valores")
plt.title("Comparação dos Valores Agrupados por Tipo de Bebida")
plt.show()

# E.1) ----------------------------
print("\nQuestao E.I:")
bebidas1985 = data.loc[data["Year"] == 1985, "Beverage Types"]
print("Coluna de Bebidas do Ano de 1985:\n", bebidas1985)

# E.2) ----------------------------
print("\nQuestao E.II:")
regiao = data.loc[data["Display Value"] > 4, "WHO region"]
print("Coluna de Região com Valores Acima de 4:\n", regiao)
