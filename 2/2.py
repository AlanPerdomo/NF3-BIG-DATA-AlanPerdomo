import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/AlanPerdomo/NF3-BIG-DATA-AlanPerdomo/main/2/cursos-prouni.csv"
data = pd.read_csv(url, encoding="latin-1")
data["curso_busca"] = data["curso_busca"].replace("MatemÃ¡tica", "Matematica")
data["grau"] = data["grau"].replace("TecnolÃ³gico", "Tecnologico")

# A) ----------------------------
print("\nQuestao A:")
colunas_notas = [
    "nota_integral_ampla",
    "nota_integral_cotas",
    "nota_parcial_ampla",
    "nota_parcial_cotas",
]
data[colunas_notas] = data[colunas_notas].fillna(0.0)

# B) ----------------------------
print("\nQuestao B:")
grupoGrau = data.groupby("grau")
for grau, grupo in grupoGrau:
    print(grau)
    print(grupo)
    print()

# C) ----------------------------
print("\nQuestao C:")
cursosInteresse = ['Matematica', 'Medicina', 'Pedagogia']

for curso in cursosInteresse:
    grupo_curso = data[data['curso_busca'] == curso]
    print(curso)
    print(grupo_curso)
    print('\n')

# D) ----------------------------
print("\nQuestao D:")
grupoEstados = data.groupby("uf_busca")
mediaNotaCortePorEstado = grupoEstados[[
    "nota_integral_ampla",
    "nota_integral_cotas",
    "nota_parcial_ampla",
    "nota_parcial_cotas",
]].mean()
print(mediaNotaCortePorEstado)

# E) ----------------------------
print("\nQuestao E:")

cursosTecnologicos = data.groupby("grau").get_group("Tecnologico")
print(cursosTecnologicos)

# F) ----------------------------
print("\nQuestao F:")
data = data.drop("cidade_filtro", axis=1)

# G) ----------------------------
print("\nQuestao G:")
cursoMedicina = data[data["nome"] == "Medicina"]
mediaMensalidade = cursoMedicina["mensalidade"].mean()

print(f"Média das mensalidades dos cursos de Medicina: R$ { mediaMensalidade:.2f}")

# H) ----------------------------
print("\nQuestao H:")
mediaNotaCorteIntegral = data.loc[data['turno'] == 'Integral', 'nota_integral_cotas'].mean()
print(f"Média das notas de corte dos cursos de tempo integral: {mediaNotaCorteIntegral:.2f}")

# I) ----------------------------
print("\nQuestao I:")
bacharelado = data[data["grau"] == "Bacharelado"]
estatisticas = bacharelado["nota_integral_ampla"].describe()
print(estatisticas)

# J) ----------------------------
print("\nQuestao J:")
colunas = ["grau", "nota_integral_cotas"]
dataFiltrado = data[colunas]

mediaNotasGrau = dataFiltrado.groupby("grau")["nota_integral_cotas"].mean()

fig, ax = plt.subplots()
mediaNotasGrau.plot(kind="bar", ax=ax)

ax.set_title("Média das Notas de Corte Integral de Cotas por Grau do Curso")
ax.set_xlabel("Grau do Curso")
ax.set_ylabel("Média das Notas de Corte Integral de Cotas")

plt.show()
