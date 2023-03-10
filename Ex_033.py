#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
Num1 = int(input('Digite o 1º Valor: '))
Num2 = int(input('Digite o 2º Valor: '))
Num3 = int(input('Digite o 3º Valor: '))

Menor = Num1
Maior = Num1

if Num2<Num1 and Num2<Num3:
    Menor = Num2
elif Num3 < Num1 and Num3<Num2:
    Menor = Num3
    
if Num2 > Num1 and Num2>Num3:
    Maior = Num2
elif Num3 > Num1 and Num3>Num2:
    Maior = Num3
    
print(f'O Menor valor é {Menor}')
print(f'O Maior valor é {Maior}')