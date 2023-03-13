#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

number = int(input('Digite o número a ser convertido: '))
print('''Escolha a base para conversão ?
1 - Binario
2 - Octal
3 - Hexadecimal''')
Conversor = int(input('Sua Opção: '))
if Conversor == 1:
    print(f'O número {number} convertido para binario é {bin(number)[2:]}')
elif Conversor == 2:
    print(f'O número {number} convertido para Octal é {oct(number)[2:]}')
elif Conversor == 3:
    print(f'O número {number} convertido para Hexadecimal é {hex(number)[2:]}')
else:
    print('Opção invalida')