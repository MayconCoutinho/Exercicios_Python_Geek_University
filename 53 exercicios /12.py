# Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de 
# conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas. 


M = int(input('Digite em milhas para converte em quilômetros: '))
K = 1.61 * M
print('{1} milhas = {0:.0f} quilômetros'.format(K,M))