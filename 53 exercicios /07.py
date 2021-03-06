# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = 5.0 *(F-32.0)/9.0, sendo C a temperatura em Celsius  
# e F a temperatura em Fahrenheit.


F =  int(input('Digite os graus em Fahrenheit para converte em Celsius: '))
C =  5.0 *(F-32.0)/9.0
print('A conversão de F°{0} Fahrenheit em Celsius é C°{1:.2f}'.format(F,C))