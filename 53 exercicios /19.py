# Leia uma valor em litros e aprente-o convertido em metros cúbicos m³. A
# fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume 
# em metros cúbicos.


L = int(input('Digite em litros para converte em m³ (metros cúbicos): '))
M = L/1000
print('{0} litros = {1} m³ (metros cúbicos)'.format(L,M))