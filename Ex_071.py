# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
#o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


Saque = int(input('Digite o valor a ser sacado: '))
Total = Saque
Nota = 50
TotalNotas = 0
while True:
    if Total >= Nota:
        Total -= Nota
        TotalNotas +=1
    else:
        if TotalNotas > 0:
            print(f'Total de {TotalNotas} cédulas de R${Nota}')
        if Nota == 50:
            Nota = 20
        elif Nota ==20:
            Nota = 10
        elif Nota == 10:
            Nota = 1
        TotalNotas = 0
        if Total == 0:
            break
print('Volte sempre')
