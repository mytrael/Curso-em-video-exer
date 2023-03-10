#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n1 = int(input('Digite um número: '))
i = 1
while i <11:
    tabuada = n1*i
    print(f'{n1} * {i} = {tabuada}')
    i = i +1