#Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Numero = int(input('Digite o Número: '))
Fatorial = Numero
contador = Fatorial - 1 
while contador != 1:
    Fatorial = Fatorial * contador
    contador = contador - 1
print(f'O fatorial de {Numero} é {Fatorial}.')