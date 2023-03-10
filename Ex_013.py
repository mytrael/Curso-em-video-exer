# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
Salario = float(input('Qual o salario do funcionario? R$'))
Aumento = Salario*0.15
NovoSalario = Salario + Aumento
print(f'O funcionario que ganhava R${Salario:2f}, com o aumento de 15%, vai receber R${NovoSalario:.2f}')