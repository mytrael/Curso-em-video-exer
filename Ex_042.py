##Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes 
Lado1 = float(input('Digite o valor do 1º Lado: '))
Lado2 = float(input('Digite o valor do 2º Lado: '))
Lado3 = float(input('Digite o valor do 3º Lado: '))

validade = 0
if Lado1<Lado2+Lado3  and Lado2 <Lado1 + Lado3 and Lado3 < Lado1 + Lado2:
    print('Essas retas PODEM FORMAR um triângulo ', end ='')
    if Lado1 == Lado2 and Lado2 == Lado3:
        print('EQUILÁTERO')
    elif Lado1 == Lado2 and Lado2 != Lado3 or Lado2==Lado3 and Lado1 != Lado2 or Lado1==Lado3 and Lado3!=Lado2:
        print('ISÓSCELES')
    elif Lado1 != Lado2 and Lado2!=Lado3 and Lado3 != Lado1:
        print('ESCALENO')
else:
    print('Essas retas NÃO PODEM FORMAR um triângulo!')
    
