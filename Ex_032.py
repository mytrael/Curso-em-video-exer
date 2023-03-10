#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
Ano = int(input('Que ano quer analizar? Digite 0 para escolher o ano atual: '))

if Ano==0:
    Ano=datetime.date.today().year

if Ano%4==0 and Ano%100 !=0 or Ano%400==0 :
    print(f'O ano de {Ano} é bissexto')
else:
    print(f'O ano de {Ano} não é bissexto')
