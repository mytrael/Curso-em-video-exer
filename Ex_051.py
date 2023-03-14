#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

First = int(input('Digite o primeiro termo de uma PA: '))
Razao = int(input('Agora informe a Razão dessa PA: '))

Decimo = First + (10-1) * Razao
for i in range(First,Decimo,Razao):
    print(i, end=' -> ')
print('Fim!')