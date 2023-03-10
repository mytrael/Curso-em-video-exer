#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Numero = int(input('Digite um numero entre 0 e 9999 :'))
Unidade = Numero % 10
Dezena = Numero //10 % 10
Centena = Numero //100 %10
Milhar = Numero //1000 % 10
print(f'Analizando o numero {Numero}')
print(f'Unidade: {Unidade}')
print(f'Dezena: {Dezena} ')
print(f'Centena: {Centena}')
print(f'Milhar: {Milhar}')