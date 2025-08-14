#Coleção imutável: Não permiteallterações ou modificações
tupla = ('Goku','Vegeta','Trunks','Gohan')
print(tupla)

#Slicing de elementos
print(tupla[1:3]) #Vegeta e Trunks
print(tupla[2:])
print(tupla[-2:]) #Trunks e Gohan

#Funções PRE PRONTAS
print(len(tupla)) #Quantidade de elementos na tupla
print(max(tupla)) #Maior elemento (ordem alfabética)
print(min(tupla)) #Menor elemento (ordem alfabética)

# Listas: Coleção totalmente mutável
lista = ['Goku','Vegeta','Trunks','Gohan']
print(lista)
lista.append('Piccolo') #Adiciona um elemento no final
lista.insert(1,'Freeza') #Adiciona um elemento na posição 1
print(lista)

#Alterando elementos
lista[0] = 'Goku SSJ'
print(lista)

#Removendo elementos
lista.remove('Freeza') #Remove o elemento Freeza

#Conjuntos: Coleção mutável, não permite elementos duplicados
conjunto = {'Goku','Vegeta','Trunks','Gohan'}
print(conjunto)

#Adicionando elementos
conjunto.add('Piccolo') #Adiciona um elemento

#Removendo elementos
conjunto.discard('Gohan') #Remove o elemento Gohan

#Dicionários: Coleção mutável, composta por pares chave-valor
pessoa = {'nome': 'Goku', 'idade': 30, 'cidade': 'Campo Belo'}
print(pessoa)

#ADD
pessoa['profissão'] = 'Guerreiro Z'  # Adiciona nova chave-valor
print(pessoa)

#Update
pessoa['idade'] = 31  # Atualiza o valor da chave 'idade'
print(pessoa)  

#Remove
del pessoa['cidade']  # Remove a chave 'cidade'