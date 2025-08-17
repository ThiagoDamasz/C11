#Exercicio 4

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])  

linhas, colunas = matriz.shape

total_elementos = linhas * colunas

if total_elementos % 2 == 0:
    print("A matriz se torna um vetor unidimensional com número par de elementos.")
else:
    print("A matriz tornar um vetor unidimensional com número ímpar de elementos.")


# Exercicio 5

np.random.seed(10)
matriz2 = np.random.randint(1, 51, size=(4, 4))

media_linhas = matriz2.mean(axis=1)
media_colunas = matriz2.mean(axis=0)
print("Média das linha:", media_linhas)
print("Média das coluna:", media_colunas)

print("Maior média das linhas:", media_linhas.max())
print("Maior média das colunas:", media_colunas.max())

valores, contagens = np.unique(matriz2, return_counts=True)

numeros_duas_vezes = valores[contagens == 2]
print("\nNúmeros que aparecem 2 vezes:", numeros_duas_vezes)