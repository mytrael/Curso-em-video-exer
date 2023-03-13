#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
#do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
AnoNascimento = int(input('Digite o Ano de Nascimento: '))
AnoAtual = date.today().year
Idade = AnoAtual - AnoNascimento
AnoAlistamento = AnoNascimento + 18
if Idade<18:
    x = 18 - Idade
    print(f'Ainda faltam {x} anos para você se alistar')
    print(f'O ano de alistamento é {AnoAlistamento}')
elif Idade > 18:
    x = Idade - 18
    print(f'Seu alistamento foi a {x} anos')  
    print(f'O ano de alistamento foi {AnoAlistamento}')  
else:
    print('Seu ano de alistamento é esse')
