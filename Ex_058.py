#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
#necessários para vencer.
import random
Escolha = 0
Tentativa = 0
NumeroEscolhido = random.randint(0, 10)
print('=/='*22)
print('''Bem vindo ao jogo da adivinhação!
Irei pensar em um numero entre 1 e 10 consegue descobrir qual é ?''')
print('=\='*22)
Dificuldade = str(input('Digite a dificuldade escolhida. [Fácil,Dificil]')).strip().upper()[0]
if Dificuldade == 'F':
    while Escolha != NumeroEscolhido:
        Escolha= int(input('Digite o valor escolhido: '))
        if Escolha > NumeroEscolhido:
            print(f'Menos...Tente Novamente!')
        elif Escolha < NumeroEscolhido:
            print('Mais...Tente Novamente')
        Tentativa = Tentativa + 1
    print(f'Você acertou em {Tentativa}!!! Parabéns!')
elif Dificuldade == 'D':
    while Escolha != NumeroEscolhido:
        Escolha= int(input('Digite o valor escolhido: '))
        print('Errou... Tente Novamente!')
        Tentativa = Tentativa + 1
    print(f'Você acertou em {Tentativa}!!! Parabéns!')
else:
    print('Dificuldade não decidida, fechando programa')