# Exercício 1
lista = ['Campeonate Mundial','Galo','Barcelona','Real Madrid','PSG','Marias']
print(lista[1:4])
print(lista[4:])
sorted_lista = sorted(lista)
sorted_lista.remove('Campeonate Mundial')
print(sorted_lista)
posicao = lista.index('Barcelona')
print(f'Posição do Barcelona: {posicao}')

# Exercício 2

loja1 = {"iPhone 15", "Galaxy S24", "Xiaomi 13", "Moto G54"}
loja2 = {"Galaxy S24", "Xiaomi 13", "Pixel 8", "OnePlus 11"}

todos_modelos = loja1 | loja2 

modelos_comuns = loja1 & loja2  

print("Modelos na Loja 1:", loja1)
print("Modelos na Loja 2:", loja2)
print("Todos os modelos disponíveis:", todos_modelos)
print("Modelos disponíveis em ambas:", modelos_comuns)

# Exercício 3
aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["media"] = float(input("Digite a média do aluno: "))


if aluno["media"] >= 50:
    aluno["situacao"] = "AP"
else:
    aluno["situacao"] = "RP"

print(aluno)

# Exercício 4
pessoa = {}

for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    pessoa[nome] = {"idade": idade, "peso": peso}

pesada = max(pessoa, key=lambda nome: pessoa[nome]["peso"])
leve = min(pessoa, key=lambda nome: pessoa[nome]["peso"])

print(f"A pessoa mais pesada é {pesada} e a mais leve é {leve}")

# Exercício 5

pessoas = []
idades = 0
mulheres_novas = 0
numero_de_pessoas = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(numero_de_pessoas):
    nome = input("nome: ")
    idade = int(input("idade: "))
    sexo = input("sexo (M/F): ").upper()

    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})
    idades += idade

    if sexo == 'F' and idade < 20:
        mulheres_novas += 1

media = idades / numero_de_pessoas

print(f"Média de idade: {media:.1f}")
print(f"Número de mulheres com menos de 20 anos: {mulheres_novas}")
