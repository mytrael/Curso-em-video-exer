
ContadorIdade = 0
ContadorSexo = 0
ContadorMulheresMenos20Anos = 0
while True:
    print('=='*10)
    print('CADASTRO DE PESSOAS')
    print('=='*10)
    Idade = int(input('Idade: '))
    if Idade > 18:
        ContadorIdade += 1
    Sexo = str(input('Sexo[M/F]: ')).strip().upper()
    while Sexo !='M' and Sexo !='F':
        Sexo = str(input('Sexo[M/F]: ')).strip().upper()
    if Sexo =='M':
        ContadorSexo +=1
    if Sexo == 'F' and Idade < 20:
        ContadorMulheresMenos20Anos += 1
    print('--'*10)
    Continua = str(input('Deseja continuar[Y/N]? ')).upper().strip()   
    while Continua != 'N' and Continua != 'Y':
        Continua = str(input('Deseja continuar[Y/N]? ')).upper().strip()
    if Continua == 'N':
        print(f'========Fim do Programa========')
        break
print(f'''Total de pessoas com mais de 18 anos: {ContadorIdade}
Total de homens: {ContadorSexo}
Total de mulheres com mais de 20 anos: {ContadorMulheresMenos20Anos}''')