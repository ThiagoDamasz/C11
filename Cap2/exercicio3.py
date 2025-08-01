sexo = input("Digite seu sexo (M/F): ")

while sexo != 'M' and sexo != 'F':
    print("Sexo inválido, digite apenas 'M' ou 'F'")
    sexo = input("Digite seu sexo (M/F): ")
print("Sexo válido")

if sexo == 'M':
    print("Você é do sexo masculino.")

elif sexo == 'F':
    print("Você é do sexo feminino.")

