#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 parta viagens mais longas.

Distancia = float(input('Digite a distancia da viagem em Km: '))
print(f'Você fará uma viagem de {Distancia}Km')
if Distancia <200:
    Valor = Distancia*0.5
else:
    Valor = Distancia*0.45
print(f'O valor da passagem é R${Valor:.2f}')