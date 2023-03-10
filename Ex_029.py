#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

VelocidadeAtual = int(input('Digite a velocidade do veiculo em km/h: '))
if VelocidadeAtual <= 80:
    print('Você está dentro da velocidade permitida!')
else:
    Multa = (VelocidadeAtual-80)*7
    print(f'Você está sendo multado por excesso de velocidade no valor de R${Multa:.2f}!')