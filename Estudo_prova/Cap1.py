import math
# 1

nome = input('Digite seu nome: ')
print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome.replace(nome, 'Do inatel'))


# 2

numero = int(input('Digite o número:'))
intervalo1 = int(input('Digite o começo do intervalo:'))
intervalo2 = int(input('Digite o final do intervalo:'))

for i in range(intervalo1, intervalo2+1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 3 

sexo = input('Digite sexo: ')

while sexo != 'M'and 'F':
    sexo = input("Valor inválido. Digite novamente (M/F): ")

    if sexo == 'M':
        print("Homem")

    if sexo == 'F':
        print("Mulher")

# 4

distancia = int(input("Digite a distância da viagem: "))

if distancia <= 200:
    preco = distancia * 0.5
    print("O preço é: ", preco)

if distancia > 200:
    preco = distancia * 0.45
    print("O preço é: ", preco)

# 5

numero = int(input('Digite um número: '))
while numero < 1000 and numero > 9999:
    print('Digite um número entre 1000 e 9999')
    numero = (input('Digite um número: '))
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10
    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")

# 6 

numerod = float(input("Entre com o número decimal: "))
print("Essa é a raiz quadrada do número:", math.sqrt(numerod))
print(f"Função teto (ceil): {math.ceil(numerod)}")
print(f"Função chão (floor): {math.floor(numerod)}")
print(f"Parte inteira: {int(numerod)}")