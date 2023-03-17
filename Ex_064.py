#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
#digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
#foi a soma entre eles (desconsiderando o flag).
Numero = int(input('Digite um Número [Digite 999 para parar]: '))
Contador = 0
Acumulador = 0
while Numero != 999:
    Contador +=1
    Acumulador += Numero
    Numero = int(input('Digite um Número [Digite 999 para parar]: ')) 
print(f'{Contador} números forar digitados e a soma de todos eles foi {Acumulador}')

