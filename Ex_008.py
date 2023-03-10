# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
M = float((input('Digite a medida em metros: ')))
Mtodm = M*10
MtoCm = M*100
MtoMM = M*1000
Mtodam = M/10
Mtohm = M/100
Mtokm = M/1000
print(f' {M}m= \n {Mtokm}km \n {Mtohm}hm \n {Mtodam}dam \n {Mtodm:.0f}dm \n {MtoCm:.0f}cm \n {MtoMM:.0f}mm')