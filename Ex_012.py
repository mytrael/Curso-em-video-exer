#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Preço = float(input('Digite o preço da mercadoria:R$ '))
PreçoComDesconto = Preço * 0.95
print(f'O preço da mercadoria é R$ {PreçoComDesconto:.2f}')
