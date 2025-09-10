import pandas as pd
import numpy as np

# Plantando a semente para números aleatórios
np.random.seed(10)

# Criando o DataFrame
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

print(df)

# 6
colunaX = df["X"] < 30

media_x = df.loc[colunaX, "X"].mean()

print("Média de X menor que 30:", media_x)

# 7
mediaD = df.loc['D'].mean()
print("Média da linha D:", mediaD)

# 8
colunasJuntas = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("Slicing da matriz:")
print(colunasJuntas)

soma_colunas = colunasJuntas.sum(axis=0)
print("Soma dos elementos de cada coluna:")
print(soma_colunas)

soma_linhas = colunasJuntas.sum(axis=1)
print("Soma dos elementos de cada linha:")
print(soma_linhas)

