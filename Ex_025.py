##Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
Nome = str(input('Digite o seu Nome Completo: '))
Silva = Nome.upper().find('SILVA')

print(f'Seu nome tem Silva ? {Silva>=0}')