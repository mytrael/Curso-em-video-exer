from random import randint

Contador = 0
while True:
    Jogador = int(input('Escolha um número de 0 a 10: '))
    PouI = str(input('Escolha Par ou impar[P/I]: ')).strip().upper()
    Computador = randint(0, 10)
    Resultado = Jogador + Computador
    if PouI== 'P':
        if Resultado%2 == 0:
            print(f'você jogou {Jogador} e eu Joguei {Computador}. O jogador Venceu!!')
            Contador += 1
        else:
            print(f'você jogou {Jogador} e eu Joguei {Computador}. O Computador Venceu!!!')
            break
    elif PouI == 'I':
        if Resultado%2 != 0:
            print(f'você jogou {Jogador} e eu Joguei {Computador}. O jogador Venceu !!!')
            Contador += 1
        else:
            print(f'você jogou {Jogador} e eu Joguei {Computador}. O Computador Venceu!!!')
            break
    else: 
        print('Opção invalida!!!')
if Contador == 1:        
    print(f'Game Over! Você venceu {Contador} vez')
elif Contador == 0:
    print(f'Game Over! Você não venceu nem uma vez')
else:
    print(f'Game Over! Você venceu {Contador} vezes')