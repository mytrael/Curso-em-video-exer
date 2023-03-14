#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
Num = int(input('Digite um número: '))
Contador = 0
for i in range(1,Num+1):
    if Num%i == 0:
        print( '\033[33m', end=' ')
        Contador += 1
    else:
        print('\033[31m', end= ' ')
    print(i, end=' ' ) 
    
print(f'\n\033[mO número {Num}, foi divisível {Contador} vezes')   
if Contador <=2:
    print(f'O número {Num} é um Número Primo')
else:
    print(f'O Número {Num} não é primo')