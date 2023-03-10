##Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente. 
Nome = str(input('Digite o seu nome Completo: ')).strip().split()
FirstName = Nome[0]
LastName = Nome[-1]
print('É um prazer te conhecer!')
print(f'Seu primeiro nome é {FirstName}')
print(f'Seu primeiro nome é {LastName}')