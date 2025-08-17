import random
import numpy as np


#Exercicio 1
arr1 = np.ones(8)
arr2 = np.random.rand(8)
resultado = arr1 + arr2

soma_elementos = np.sum(resultado)

if soma_elementos >= 40:
    matriz = resultado.reshape(4, 2)
else:
    matriz = resultado.reshape(2, 4)

print("Matriz final:\n", matriz)    

#Exercício 2

arr_pares1 = np.arange(0, 51, 2)
arr_pares2 = np.arange(100, 51, -2)

concatenar = np.concatenate((arr_pares1, arr_pares2))

ordenar = np.sort(concatenar)

print('Arrays concatenados:', ordenar)

#Exercicio 3

mtz_0s = np.zeros(4).reshape(2, 2)
print("Matriz de 0s:", mtz_0s)

linha = random.randint(0, 1)
coluna = random.randint(0, 1)
mtz_0s[linha, coluna] = 1


tentativas = 0 
achou = False  

while tentativas < 3:
    pos = input(f"Digite a posição (linha coluna): ")
    i, j = map(int, pos.split())

    if mtz_0s[i, j] == 1:
        print("Game Over! :( Try Again!")
        achou = True
        break
    
    tentativas += 1

if not achou:
    print("Congratulations! You beat the game! :)")
