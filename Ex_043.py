#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida 

Peso = float(input('Digite o Peso: '))
Altura = float(input('Digite a Altura em metros: '))

Imc = Peso/(Altura**2)

if Imc < 18.5:
    print(f'O individuo está abaixo do peso, seu IMC é {Imc}')
elif Imc <= 25:
    print(f'O individuo está no peso Ideal, seu IMC é {Imc}')
elif Imc <= 30:
    print(f'O individuo está com sobrepeso, seu IMC é {Imc}')
elif Imc <= 40:
    print(f'O individuo está com obesidade, seu IMC é {Imc}')
else:
    print(f'O individuo está com Obesidade Mórbida, seu IMC é {Imc}')