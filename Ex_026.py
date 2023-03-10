#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

Frase = str(input('Digite Uma Frase: ')).strip().upper()

QuantidadeDeAs = Frase.count('A')
print(f'A Letra a aparece {QuantidadeDeAs} na frase')
FirstA = Frase.find('A') +1
print(f'O primeiro A aparece na posição: {FirstA}')
LastA = Frase.rfind('A') + 1
print(f'O ultimo A aparece na posição: {LastA}')