#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).

Contador = Soma = 0
while True:
    Valor = int(input('Digite um valor[999 para parar]: '))
    if Valor == 999:
        break
    Contador +=1
    Soma += Valor
    
print(f'A soma dos {Contador} valores foi {Soma}')
