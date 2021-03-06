# Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
# A fórmula de conversão é: P = C/2,54,sendo C o comprimento em centímetros e P o
# comprimento em polegadas.


C = int(input('Digite em centímetros para converte em polegadas: '))
P = C/ 2.54
print('{0} centímetros = {1:.2f} polegadas'.format(C,P)) 