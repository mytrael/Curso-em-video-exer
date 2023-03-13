from datetime import date

ThisYear = date.today().year
Maioridade = 0

for i in range(7):
    Age = int(input('Digite O ano de nascimento:'))
    if  ThisYear - Age >= 21:
        Maioridade +=1
print(Maioridade)
