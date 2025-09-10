import numpy as np

ds = np.loadtxt(r"C:\Users\Thiag\Downloads\paises(1).csv", delimiter=';', dtype=str, encoding='utf-8')

#1
paises = ds[1:, 0]
regiao = ds[1:, 1]
pop = ds[1:, 2]
area = ds[1:, 3]

print(paises, '\n')
print(regiao, '\n')
print(pop, '\n')
print(area, '\n')

#2

regiao_unica = np.unique(regiao)

print('Regiões unicas: ', regiao_unica)


#3
alfabetizacao = ds[1:, 9].astype(float)

media = np.mean(alfabetizacao)

print("Media da alfabetizacao: ", media)

#4
num_AN = np.char.find(regiao, 'NORTHERN AMERICA') >= 0
print('Paises da America do Norte: ', sum(num_AN), '\n')

#5
num2 = ds[1:, 8].astype(float)
 
gdp = num2[regiao == 'LATIN AMER. & CARIB']
 
print('O maior GPD da Ameria Latina e Caribe: ', gdp)