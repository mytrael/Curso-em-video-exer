#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
x = float(input('Digite um número Real '))
truncado = math.trunc(x)
print(f'A porção inteira de {x} é {truncado}')