#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
#entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
#se ele quer ou não continuar a digitar valores.
Continuar = 'S'
Contador = Soma = Media = Maior = Menor = 0
while Continuar == 'S':
    Numero = int(input('Digite um número: '))
    Contador +=1
    if Contador == 1:
        Maior = Menor = Media = Numero
    else:
        if Numero > Maior:
            Maior = Numero
        elif Numero < Menor:
            Menor = Numero   
    Soma += Numero
    Continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
Media = Soma/Contador

print(f'''Você digitou {Contador} Números,
a media entre eles foi {Media:.2f},
sendo o maior número {Maior}, e o menor número {Menor}''')
    
