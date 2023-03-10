#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
Valor = float(input('Valor do imovel: '))
Salario = float(input('Salario do comprador: '))
Ano = int(input('Anos de financiamento: '))

PrestacaoMensal = Valor/(Ano*12)
print(f'Para pagar um imovel no valor de {Valor:.2f}, em {Ano} anos dará uma parcela mensal de {PrestacaoMensal:.2f}')
if PrestacaoMensal >= Salario*0.3:
    print('Infelizmente, você não poderá pegar esse emprestimo!')
else:
    print('Emprestimo concedido')

