#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

Sexo = str(input('digite seu Sexo [M,F]: ')).strip().upper()[0]
while Sexo not in 'MFmf':   
    print('Não reconheço essa Opção. Por favor digite novamente.')
    Sexo = str(input('Digite seu Sexo[M,F]: ')).strip().upper()[0]
print(f'Sexo {Sexo} registrado com sucesso.')
print('FIM!')