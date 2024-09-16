'''A prefeitura de uma cidade fez uma pesquisa com 200 pessoas, coletando dados sobre o salário e o número de filhos.
A prefeitura deseja saber: • A média do salário dessas pessoas • A média do número de filhos • O maior salário'''

contador = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0

while contador < 3:
    salario = float (input("Informe o salario por favor: "))
    n_filhos = int(input("Informe o número de filhos: "))
    contador += 1

soma_salarios += salario
soma_filhos += n_filhos

if salario > maior_salario:
    maior_salario = salario
    contador += 1
media_salarios = soma_salarios / 200
media_filhos = soma_filhos /200

print("Média do salario é :", media_salarios)
print("Média de número de filhos", media_filhos)
print("Maior salario: ", maior_salario)
