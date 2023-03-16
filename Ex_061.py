#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

FirstTerm = int(input('Digite o 1º termo de uma PA: '))
Razao = int(input('Digite a razão: '))
contador = 0
while contador <10:
    print(FirstTerm, end = ' ')
    FirstTerm = FirstTerm + Razao
    contador += 1
    
print('Fim')