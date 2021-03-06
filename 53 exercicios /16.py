# Leia uma valor de comprimento em polegadas e apresente-o convertido em centímetros.
# A fórmula de conversão é: C = P *2,54,sendo C o comprimeto em centimetros e P o 
# comprimento em polegadas.


P = int(input('Digite em polegadas para converte em centímetros: '))
C = P * 2.54
print('{0} polegadas = {1} centímetros'.format(P,C))