# Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = k - 273.15, sendo C a temperatura em Celsius e K 
# a temperatura em Kelvin.


K = int(input('Digite a temperatura em Kelvin para converte em Celsius: '))
C = K - 273.15
print('A conversão de {0} Kelvin em Celsius é C°{1:.2f}'.format(K,C))