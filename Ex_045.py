#Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random
print(''' Suas Opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

Player = int(input('Digite sua jogada: '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')

if Player ==1:
    print('Você jogou Pedra')
elif Player ==2:
    print('Você jogou Papel')   
else:
    print('Você jogou Tesoura')
    
Computer = random.randint(1, 3)
if Computer ==1:
    print('Computador jogou Pedra')
elif Computer ==2:
    print('Computador jogou Papel')   
else:
    print('Computador jogou Tesoura')
    
if Player>Computer:
    if Player==3 and Computer==1:
        print('Computador Venceu!!!!')
    else:
        print('Jogador Venceu!!!!')
elif Computer>Player:
    if Computer==3 and Player==1:
        print('Jogador Venceu!!!!')
    else:
        print('Computador Venceu!!!!')
elif Computer == Player:
    print('Empate técnico!')
    