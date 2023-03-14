#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
Maior = 0
Menor = 0
for i in range(1,6):
    Peso = float(input(f'Digite o Peso da {i} pessoa: '))
    if i == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
        elif Peso < Menor:
            Menor = Peso
print(f'O maior peso foi de {Maior}Kg, e o menor peso foi de {Menor}Kg')      