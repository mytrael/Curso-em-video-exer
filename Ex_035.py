#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.
print("-=-"*10)
print('Analisador de Triângulo')
print("-=-"*10)
Lado1 = float(input('Digite o valor do 1º Lado: '))
Lado2 = float(input('Digite o valor do 2º Lado: '))
Lado3 = float(input('Digite o valor do 3º Lado: '))

validade = 0
if Lado1<Lado2+Lado3  and Lado2 <Lado1 + Lado3 and Lado3 < Lado1 + Lado2:
    print('Essas retas podem formar um triângulo! ')
else:
    print('Essas retas não podem formar um triângulo!')





