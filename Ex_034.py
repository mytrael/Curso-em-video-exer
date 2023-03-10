#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00,calcule um aumento de 10%. Para os inferiores ou iguais,
#o aumento é de 15%.
Salario = float(input('Digite o valor do seu salário: R$'))

if Salario >= 1250:
    Salario = Salario + Salario*0.10
else:
    Salario = Salario + Salario*0.15  
print(f'O Novo salário é de R${Salario:.2f}')