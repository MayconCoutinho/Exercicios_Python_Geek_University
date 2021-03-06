# Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s 
# (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em 
# km/h e M em m/s. 

K = int(input('Digite em km/h para converte em m/s: '))
M = K/3.6 
print('A conversão: {0}km/h = {1:.2f}m/s'.format(K,M)) 