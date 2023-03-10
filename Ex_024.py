##Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

Cidade = str(input('Digite o nome da Cidade: ')).strip()
print(Cidade[:5].lower() =='santo')
