#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
#elementos de uma Sequência de Fibonacci.
print('-=-'*15)
print('Sequencia Fibonacci')
print('-=-'*15)
UltimoElemento = int(input('Quantos elementos da sequencia você quer mostrar? '))
Elemento = 0
Sucessor = 1
Antecessor = 1
while Elemento < UltimoElemento:
    if Elemento == 0:
        print('0', end= ' ->')
    elif Elemento <= 2:
        print('1', end= ' ->')
    else:
        Resultado = Sucessor + Antecessor
        Antecessor = Sucessor
        Sucessor = Resultado
        print(Resultado, end= ' ->')
    Elemento +=1
print('Fim')