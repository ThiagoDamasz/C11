import numpy as np
arr1 = np.arange(1, 10, 1)
arr2 = np.arange(9, 0, -1)

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Soma dos arrays:", arr1 + arr2)

#CONCATENAÇÃO
arr_concat = np.concatenate([arr1, arr2])
print("Array concatenado:", arr_concat)

#OPERACOES COM MATRIZES
mtz = np.array([50,10,100,60,25,100,75,80,100]).reshape(3,3)
print(mtz)

print(mtz.sum(axis=1))

#Broadcasting
print(mtz/10)