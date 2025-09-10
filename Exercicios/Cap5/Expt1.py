import pandas as pd

# 1
serie1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
serie2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print("Série Ano 1:")
print(serie1)
print("Série Ano 2:")
print(serie2)

# 2
total1 = serie1.sum()
total2 = serie2.sum()

print(f"Total Ano 1: {total1}")
print(f"Total Ano 2: {total2}")

# 3

crescimento = serie2 - serie1
print(f"Crescimento de um ano para o outro: {crescimento}")

# 4
cresceram = crescimento[crescimento > 0]
print(f"Linguagens que cresceram: {cresceram}")

# 5 

projecao = serie2 + (2 * crescimento)
print(f"Projeção para daqui 2 anos: {projecao}")