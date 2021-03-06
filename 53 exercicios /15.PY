# Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversâo
# é G = R * 180/π, sendo G o ângulo em graus e R em radianos e π = 3.14. 


R = float(input('Digite em radiano para converte em graus: '))
G = R * 180/3.14
print('{0} radianos = {1:.2f} graus'.format(R,G))