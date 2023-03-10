#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
L = float(input('Digite a largura: '))
H = float(input('Digite a altura: '))
A= L*H
tinta = A/2

print(f'A área é {A}m2, e a quantidade de tinta é {tinta}L')