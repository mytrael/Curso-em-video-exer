#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
Nome = input('Digite seu nome completo: ').strip()
print('Analizando...')
print(f'Nome todo em maiusculo: {Nome.upper()}')
print(f'Nome todo em minusculo: {Nome.lower()}')
Nomeletters = len(Nome)-Nome.count(' ')
print(f'Quantidade de letras no seu nome: {Nomeletters}')
NameSplit = Nome.split()
print(f'quantidade de letras no 1º nome: {len(NameSplit[0])}')