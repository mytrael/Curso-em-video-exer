

Contador = Soma = 0
while True:
    Valor = int(input('Digite um valor[999 para parar]: '))
    if Valor == 999:
        break
    Contador +=1
    Soma += Valor
print(f'A soma dos {Contador} valores foi {Soma}')
