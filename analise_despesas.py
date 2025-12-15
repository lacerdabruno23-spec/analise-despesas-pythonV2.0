import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv("despesas.csv")

# Converter coluna de data
df["data"] = pd.to_datetime(df["data"])

# Agrupar despesas por categoria
resumo = df.groupby("categoria")["valor"].sum()

# Mostrar resumo no terminal
print("\nResumo de despesas por categoria:\n")
print(resumo)

# Criar gráfico
resumo.plot(kind="bar")
plt.title("Despesas por Categoria - Janeiro")
plt.xlabel("Categoria")
plt.ylabel("Valor (R$)")
plt.tight_layout()

# Mostrar gráfico
plt.show()
