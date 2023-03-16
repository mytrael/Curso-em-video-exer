#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso. 
import time 

option = 0
Valor1 = int(input('Digite o 1º Valor: '))
Valor2 = int(input('Digite o 2º Valor: '))
while option !=5:
    print('''Digite a opção que deseja:
          [ 1 ]Somar
          [ 2 ]Multiplicar
          [ 3 ]Maior
          [ 4 ]Menor
          [ 5 ]Sair do programa''')
    option = int(input('Digite aqui: '))
    if option == 1:
        Resultado = Valor1 + Valor2
        print(f' a soma de {Valor1} com {Valor2} é {Resultado}')
        time.sleep(2)
    elif option == 2:
        Resultado = Valor2 * Valor1
        print(f'O produto de {Valor1} com {Valor2} é {Resultado}')
        time.sleep(2)
    elif option == 3:
        if Valor1 > Valor2:
            print(f'O {Valor1} é maior que {Valor2}')
        elif Valor2 > Valor1:
            print(f'O {Valor2} é maior que {Valor1}')
        else:
            print('Os valores são iguais')
        time.sleep(2)
    elif option == 4:
        if Valor1 < Valor2:
            print(f'O {Valor1} é menor que {Valor2}')
        elif Valor2 < Valor1:
            print(f'O {Valor2} é menor que {Valor1}')
        else:
            print('Os valores são iguais')
        time.sleep(2)
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, escolha uma opção!')