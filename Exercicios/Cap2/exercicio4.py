distancia = float(input("Digite a distância em KM: "))

if distancia < 200:
    preco = distancia * 0.50
    print("O preço da passagem é: R$", preco)

else:
    preco = distancia * 0.45
    print("O preço da passagem é: R$", preco)