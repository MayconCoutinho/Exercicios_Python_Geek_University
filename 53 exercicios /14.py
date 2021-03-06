# Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
# é: R = G* π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.


G = int(input('Digite em graus para converte em radiano: '))
R = G* 3.14/180
print('{0} graus = {1:.3f} radianos'.format(G,R))