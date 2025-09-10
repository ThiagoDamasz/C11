import numpy as np

# Carrega dataset
dataset = np.loadtxt(
    r'C:\Users\Thiag\OneDrive\Documentos\C11\Estudo_prova\space (1).csv', 
    delimiter=';', 
    dtype=str,
    encoding='utf-8',
    skiprows=1,
)

# 1) Porcentagem de missões que deram certo
status = dataset[:, -1]  
sucessos = np.sum(status == "Success")
porcentagem = (sucessos / len(status)) * 100
print(f"1) Porcentagem de missões que deram certo: {porcentagem:.2f}%")

# 2) Média dos gastos (>0)
costs = np.char.strip(dataset[:, 6]).astype(float)
costs_validos = costs[costs > 0]
media_custos = np.mean(costs_validos)
print(f"2) Média dos custos válidos: {media_custos:.2f}")

# 3) Missões realizadas nos EUA
location = dataset[:, 2]
missoes_usa = np.sum(np.char.find(location, "USA") >= 0)
print(f"3) Total de missões realizadas nos EUA: {missoes_usa}")

# 4) Missão mais cara da SpaceX
company = dataset[:, 1]
custos_spacex = costs[np.char.find(company, "SpaceX") >= 0]
max_spacex = np.max(custos_spacex)
print(f"4) Maior valor de missão da SpaceX: {max_spacex}")

# 5) Empresas e quantidade de missões
empresas, quantidades = np.unique(company, return_counts=True)
print("5) Empresas e suas quantidades de missões:")
for nome, qtd in zip(empresas, quantidades):
    print(f"   {nome}: {qtd}")
