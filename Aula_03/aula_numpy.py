import numpy as np

#1D
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print(type(arr))

#2D
mtz = np.array([[1,2,3], [4,5,6]])
print("Matriz:", mtz)

#FUNÇÕES PARA ESTRUTURAR NUMPY ARRAYS
#ARRAY 1D de 1s
arr_1s = np.ones(5)
print("Array de 1s:", arr_1s)

#ARRAY 2D de 0s com reshape
mtz_0s = np.zeros(10).reshape(5, 2)
print("Matriz de 0s:", mtz_0s)

#ARANGE
arr_arange = np.arange(10,101,10)
print("Array com arange:", arr_arange)

# menor valor
print("Menor valor:", arr_arange.min())

# maior valor
print("Maior valor:", arr_arange.max())

# média
print("Média:", arr_arange.mean())

# indice do maior valor
print("Índice do maior valor:", arr_arange.argmax())

# indice do menor valor
print("Índice do menor valor:", arr_arange.argmin())
