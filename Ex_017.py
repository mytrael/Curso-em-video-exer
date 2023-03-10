#aça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
CO = float(input('Comprimento do Cateto Oposto: '))
CA = float(input('Comprimento do Cateto Adjacente: '))
TG = hypot(CO,CA)

print(f'O comprimento da tangente é: {TG:.2f}')
