#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
Dias = int(input('quantos dias o carro ficou alugado ? '))
Km = float(input('Quantos Km foram rodados ? '))
Valor = 60*Dias + 0.15*Km

print(f'o valor a ser pago é de R${Valor:.2f}')