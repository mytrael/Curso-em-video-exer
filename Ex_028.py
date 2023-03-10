# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
NumeroEscolhido = random.randint(0, 5)
print('==='*32)
print('''Bem vindo ao jogo da adivinhação, irei pensar em um numero de 1 a 5 consegue descobrir qual é ?''')
print('==='*32)
Escolha= int(input('Digite o valor escolhido: '))

print('Processando')
time.sleep(2)

if Escolha == NumeroEscolhido:
    print('Você acertou!!! Parabéns!')
else:
    print(f'Errooou! O número certo era {NumeroEscolhido} Tente Novamente.')
