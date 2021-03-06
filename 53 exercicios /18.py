# Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A 
# fórmula de conversão é: L = 1000 * M, sendo L o velume em litros e M o volume em 
# metros cúbicos.


M = int(input('Digite em metros cúbicos m³ para converte em litros: '))
L = 1000*M 
print('{1}m³ (metros cúbicos) = {0}l (litros)'.format(L,M))