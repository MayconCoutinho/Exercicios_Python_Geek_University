# Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
# A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H 
# a área em hectares.


H = int(input('Digite em hectare para converte em metros quadrados: '))
M = H *10000
print('{0} hectare = {1} metros quadrados'.format(H,M))