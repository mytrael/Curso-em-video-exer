#: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos. 

FirstTerm = int(input('Digite o 1º termo de uma PA: '))
Razao = int(input('Digite a razão: '))
Contador = 0
Contador2 = 10
var1 = 1
while Contador <Contador2:
    print(FirstTerm, end = ' ')
    FirstTerm = FirstTerm + Razao
    Contador += 1
while var1 != 0:
    var1 = int(input('\nQuantos termos a mais você quer contar? '))
    Contador2 += var1
    while  Contador < Contador2:
        print(FirstTerm, end = ' ')
        FirstTerm = FirstTerm + Razao
        Contador += 1
print(f'Progressão finalizada com {Contador} termos contados')