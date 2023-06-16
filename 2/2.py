import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/AlanPerdomo/NF3-BIG-DATA-AlanPerdomo/main/2/cursos-prouni.csv"
data = pd.read_csv(url,encoding='latin-1')

# A)
colunas_notas = [
    "nota_integral_ampla",
    "nota_integral_cotas",
    "nota_parcial_ampla",
    "nota_parcial_cotas",
]
data[colunas_notas] = data[colunas_notas].fillna(0.0)

# B)
grupo_grau = data.groupby("grau")

# C)
cursos = ["Matemática", "Medicina", "Pedagogia"]
dataC = data[data["nome"].isin(cursos)]
grupoCurso = dataC.groupby("nome")

# for nome, grupo in grupoCurso:
#    print(f"Dados para o curso {nome}:")
#    print(grupo)
#    print("\n")

# D)
mediaNotaCorte = data.groupby("uf_busca")["nota_integral_ampla"].mean()

# E)
cursosTecnologicos = data[data["grau"] == "Tecnológico"]
grupoTecnologicos = cursosTecnologicos.groupby("nome")

# F)
data = data.drop("cidade_filtro", axis=1)

# G)
cursoMedicina = data[data["nome"] == "Medicina"]
mediaMensalidade = cursoMedicina["mensalidade"].mean()

print(f"Média das mensalidades dos cursos de Medicina: R$ { mediaMensalidade:.2f}")

# H)
cursosTempoIntegral = data[data["turno"] == "Integral"]
mediaNotaCorteIntegral = cursosTempoIntegral["nota_integral_ampla"].mean()

print(
    f"Média das notas de corte dos cursos de tempo integral: {mediaNotaCorteIntegral:.2f}"
)

# I)
bacharelado = data[data["grau"] == "Bacharelado"]
estatisticas = bacharelado["nota_integral_ampla"].describe()
print(estatisticas)

# J)
colunas = ["grau", "nota_integral_cotas"]
dataFiltrado = data[colunas]

mediaNotasGrau = dataFiltrado.groupby("grau")["nota_integral_cotas"].mean()

fig, ax = plt.subplots()
mediaNotasGrau.plot(kind="bar", ax=ax)

ax.set_title("Média das Notas de Corte Integral de Cotas por Grau do Curso")
ax.set_xlabel("Grau do Curso")
ax.set_ylabel("Média das Notas de Corte Integral de Cotas")

plt.show()
