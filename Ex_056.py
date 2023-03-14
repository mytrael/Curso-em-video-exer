#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
AddAge = 0
MaxAge = 0
Less20 = 0
NameOld = ''
for i in range(1,5):
    print(f'-------{i} Pessoa-------')
    Name = input('Nome: ').strip().upper()
    Age = int(input('Idade: '))
    Gender = input('Gênero(M,F): ').upper().strip()
    if Gender == 'M':
        if MaxAge < Age:
            MaxAge = Age
            NameOld = Name
    if Gender == 'F' and Age < 20:
        Less20 = Less20 + 1
    AddAge =AddAge + Age
    
print(f'A Média das idade é {AddAge/4:.1f}')
print(f'O Homem com maior idade {MaxAge} e se chama {NameOld}')
print(f'Há {Less20} mulheres com menos de 20 anos')