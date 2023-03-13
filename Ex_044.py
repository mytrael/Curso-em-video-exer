#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
PrecoBruto = float(input('Digite o total em Compras R$: '))
print('''Formas de pagamento
[ 1 ]à vista dinheiro/cheque
[ 2 ]à vista no cartão
[ 3 ]em até 2x no cartão:
[ 4 ]3x ou mais no cartão:''')
Pagamento = float(input('Escolha a forma de pagamento: '))
if Pagamento == 1:
    Preco = PrecoBruto - (PrecoBruto*0.1)
elif Pagamento == 2:
    Preco = PrecoBruto - (PrecoBruto*0.05)
elif Pagamento == 3:
    Preco = PrecoBruto
    PrecoAPagar = Preco/2
    print(f'Sua compra será parcelada de 2x de R${PrecoAPagar:.2f} com Juros')
elif Pagamento == 4:
    Parcela = int(input('Quantas parcelas? '))
    Preco = (PrecoBruto + (PrecoBruto*0.2))
    PrecoAPagar = Preco/Parcela 
    print(f'Sua compra será parcelada de {Parcela}x de R${PrecoAPagar:.2f}')
else:
    print('Opção invalida!')
print(f'Sua compra de {PrecoBruto:.2f} vai custar {Preco:.2f}')