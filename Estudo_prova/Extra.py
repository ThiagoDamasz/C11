import numpy as np

dataset = np.loadtxt(
    r'C:\Users\Thiag\OneDrive\Documentos\C11\Estudo_prova\paises(1).csv', 
    delimiter=';', 
    dtype=str,
    encoding='utf-8',
    skiprows=1,
)

#1
pais = dataset[:, 0]  
region = dataset[:, 1]
population = dataset[:, 2]  
area = dataset[:, 3]    

print("País: ", pais)
print("Região: ", region)
print("População: ", population)
print("Área: ", area)

#2

regioes_unicas = np.unique(region)
print("Quantidade de regiões diferentes:", len(regioes_unicas))
print("Regiões encontradas:", regioes_unicas)

#3

alfabetizacao = dataset[:, 9].astype(float) 
alf_valido = alfabetizacao[alfabetizacao > 0]
media_alf = np.mean(alf_valido)
print("Taxa média de alfabetização: ", media_alf)

#4

paises_EUA = np.sum(np.char.find(region, "NORTHERN AMERICA") >= 0)
print(f"3) Total paises norte americanos: {paises_EUA}")

#5 maior renda per capta

gdp = dataset[:, 8].astype(float)

idx = np.argmax(gdp[region == "LATIN AMER. & CARIB    "])
print(pais[region == "LATIN AMER. & CARIB    "][idx])