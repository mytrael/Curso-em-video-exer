#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
Aluno1 = input('Digite o nome do primeiro aluno: ')
Aluno2 = input('Digite o nome do segundo aluno: ')
Aluno3 = input('Digite o nome do terceiro aluno: ')
Aluno4 = input('Digite o nome do quarto aluno: ')

seq = [Aluno1,Aluno2,Aluno3,Aluno4]

random.shuffle(seq)
print(f'A ordem de apresentação é :')
print(seq)