#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

Nota1 = float(input('digite a primeira nota do Aluno: '))
Nota2 = float(input('digite a segunda nota do Aluno: '))
Media = (Nota1 + Nota2)/2
print(f'Tirando {Nota1:.1f} e {Nota2:.1f} a Media do aluno foi {Media:.2f}')
if Media <=5 and Media >0:
    print('Reprovado')
elif Media > 5 and Media <7:
    print('Recuperação')
elif Media>=7 and Media<10:
    print('Aprovado')
else:
    print('Nota invalida')