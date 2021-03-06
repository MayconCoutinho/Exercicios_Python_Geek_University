# Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = C * (9.0/5.0)+32.0,sendo F a temperatura em Celsius
# e F a temperatura em Fahrenheit.


C = int(input('Digite a temperatura em C° para converte em  F°: '))
F = C * (9.0/5.0)+32.0 
print('A conversão de C°{0} Celsius para Fahrenheit é F°{1:.0f}'.format(C,F))