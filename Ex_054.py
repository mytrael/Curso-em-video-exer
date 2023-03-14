#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ThisYear = date.today().year
Maioridade = 0

for i in range(1,8):
    Age = int(input(f'Em que ano a {i} pessoa nasceu:'))
    if  ThisYear - Age >= 21:
        Maioridade +=1
print(f'{Maioridade} pessoas alcançarama maioridade\n{7-Maioridade} ainda não alcançaram')
