###Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
###– O primeiro valor é maior
###– O segundo valor é maior
###– Não existe valor maior, os dois são iguais
Number1 = float(input('Digite o primeiro número: '))
Number2 = float(input('Digite o primeiro número: '))                  

if Number1 > Number2:
    print('O primeiro valor é maior')
elif Number2 > Number1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')