# Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
# (quilômetros pro hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
# em km/h e M em m/s 


M =  int(input('Digite em m/s para converte em km/h: '))
K = M* 3.6
print('{0}m/s = {1:.0f}km/h '.format(M,K))