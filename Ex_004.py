#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ele.
x = input('digite algo: ')
print(f'o tipo primitivo desse valor é ',type(x))
print(f'{x} é apenas númeroC?', x.isnumeric())
print(f'{x} são apenas letras?', x.isalpha())
print(f'{x} é alphanumerico? ', x.isalnum())
print(f'{x} está em maiúsculo ?', x.isupper())
print(f'{x} está em minusculo?', x.islower())
print(f'{x} Só tem espaço?', x.isspace())
print(f'{x} está capitalizado (titulo)?', x.istitle())