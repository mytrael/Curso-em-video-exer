Soma = 0
Contador = 0
for c in range(1,501,2):
    if c%3 == 0:
        Contador += 1
        Soma += c
print(f' O valor da soma dos números solicitados é {Soma} e foram {Contador} números somados')