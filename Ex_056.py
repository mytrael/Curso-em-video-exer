AddAge = 0
for i in range(4):
    Name = input('Digite o Nome: ')
    Age = int(input('Digite o valor da idade: '))
    Gender = input('Digite o Gênero(M,F): ').upper()
    AddAge =AddAge + Age
    
print(f' A Média das idade é {AddAge/4}')