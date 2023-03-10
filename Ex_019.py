#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
Aluno1 = input('digite o nome do primeiro aluno: ')
Aluno2 = input('digite o nome do segundo aluno: ')
aluno3 = input('digite o nome do terceiro aluno: ')
Aluno4 = input('digite o nome do quarto aluno: ')

seq = [X,y,w,z]
escolhido = choice(seq)

print(f'O aluno escolhido foi {escolhido}')