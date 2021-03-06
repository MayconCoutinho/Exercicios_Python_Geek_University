# Leia uma distância em quilômetros e apresente-a convertida em minlhas. A fórmula de
# conversão é: M = K/1,61, sendo K a distância em quilômetros e M em milhas.


K = int(input('Digite em quilômetros para converte em milhas: '))
M = K/1.61
print('{0} quilômetros = {1:.0f} milhas'.format(K,M))