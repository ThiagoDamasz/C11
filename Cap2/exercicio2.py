numero =  int(input('Digite um número: '))

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")