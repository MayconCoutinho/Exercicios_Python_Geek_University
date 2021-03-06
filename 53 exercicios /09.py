# Leia uma temparatura em graus Celsius apresente-a convertida em graus Kelvin. A fórmula de conversão é:
# K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura en Kelvin.


C = int(input('Digite a temperatura em graus Celsius para converte em Kelvin: '))
K = C + 273.15
print('A conversão de C°{0} Celsius em Kelvin é {1}'.format(C,K))