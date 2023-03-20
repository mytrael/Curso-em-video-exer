

Contadormais1000 = 0
TotalGasto = 0
MaisBaratoNome = ''
MaisBaratoPreco = 0
while True:
    Nome = str(input('Digite o nome do produto: ')).strip()
    Preco = float(input('Digite o Preço R$: '))
    if MaisBaratoNome =='':
        MaisBaratoNome = Nome
        MaisBaratoPreco = Preco
    elif MaisBaratoPreco > Preco:
        MaisBaratoNome = Nome
        MaisBaratoPreco = Preco
    if Preco >= 1000:
        Contadormais1000 +=1
    TotalGasto += Preco
    Continua = str(input('Deseja continuar> [S/N] ')).strip().upper()
    if Continua == 'N':
        print('Finalizando Compra')
        break
    
print(f'''Total Gasto =R${TotalGasto:.2f}
Houve {Contadormais1000} item/itens custando mais de R$1000.00
O produto mais barato foi {MaisBaratoNome} que custou {MaisBaratoPreco:.2f}''')