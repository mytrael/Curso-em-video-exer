#Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
import math

angulo = int(input('Digite o valor do angulo em graus: '))
anguloemradianos = math.radians(angulo)
seno = math.sin(anguloemradianos)
cosseno = math.cos(anguloemradianos)
tangente = math.tan(anguloemradianos)

print(f'O Seno de {angulo}º, vale {seno:.2f}, o cosseno vale {cosseno:.2f}, e a tangente vale {tangente:.2f}')