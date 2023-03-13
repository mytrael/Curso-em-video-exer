# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
Soma = 0
for i in range(6):
    Num = int(input('Digite um Valor: '))
    if Num%2==0:
        Soma += Num
print(f' A soma dos números pares foi {Soma}')