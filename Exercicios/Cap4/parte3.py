import pandas as pd
import numpy as np

#Achei mais simples importar o dataFrame com Pandas e fazer as contas com o numpy
dataFrame = pd.read_csv("C:/Users/Thiag/Downloads/space (1).csv", delimiter = ";") 

print(dataFrame.columns)

# Exercício 1
status_mission = dataFrame["Status Mission"].to_numpy()

total_missoes = len(status_mission)
sucessos = np.sum(status_mission == "Success")
porcentagem = (sucessos / total_missoes) * 100
print("Essa é a porcentagem das que deram certo:",porcentagem)

#Exercício 2
cost = dataFrame[" Cost"].to_numpy()

cost_resposta = cost[cost>0]

media = np.mean(cost_resposta)
print("Media dos gastos: ", media)

#Exercício 3
location = dataFrame["Location"].to_numpy().astype(str)

nosEua = np.sum(np.char.find(location,"USA"))
print("Missões nos EUA: ",nosEua)

#Exercício 4
detail = dataFrame["Detail"].to_numpy()
df_spacex = dataFrame[dataFrame["Company Name"] == "SpaceX"]
cost_spacex = df_spacex[" Cost"].to_numpy()
detail_spacex = df_spacex["Detail"].to_numpy()

indiceMaisCaro = np.argmax(cost_spacex)
print("Essa foi a missão mais cara: ", detail_spacex[indiceMaisCaro])

#Exercício 5
companies = dataFrame["Company Name"].to_numpy()
empresas_unicas = np.unique(companies)

for empresa in empresas_unicas:
    qtd = np.sum(companies == empresa)
    print(f"{empresa}: {qtd} missões")
