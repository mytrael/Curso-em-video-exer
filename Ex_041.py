#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
import datetime
Nascimento = int(input('Digite o ano de nascimento do atleta: '))
AnoAtual = datetime.date.today().year
Idade = AnoAtual-Nascimento
print(f'A idade do Atleta é {Idade}')
if Idade <= 9:
    print('Atleta MIRIM')
elif Idade <= 14:
    print('Atleta INFANTIL')
elif Idade <= 19:
    print('Atleta JÚNIOR')
elif Idade <= 25:
    print("Atleta SÊNIOR")
else:
    print('Atleta MASTER')