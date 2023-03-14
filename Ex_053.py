#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços. Exemplos de palíndromos:

Frase = input('Digite uma frase: ').upper().strip()
Palavra = Frase.split()
junto = ''.join(Palavra)
inverso =''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um Palíndromo')
else:
    print('Não temos um Palíndromo')    
