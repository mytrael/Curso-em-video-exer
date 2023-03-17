print('=='*10)
print('Tabuada')
print('=='*10)
while True:
    Tabuada = int(input('Quer saber a tabuada de qual número? '))
    if Tabuada <= 0:
        print('Encerrando Programa !!!')
        break
    Contador = 1
    print('=/='*5)
    print(f'Tabuada de {Tabuada}')
    print('=\='*5)
    while Contador <= 10:
        Resultado = Contador * Tabuada
        print(f'{Contador} * {Tabuada} = {Resultado}')
        Contador += 1