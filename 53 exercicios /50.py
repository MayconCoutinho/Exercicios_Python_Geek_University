# Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua
# distância da oreigem (0,0)

x = float(input('Digite a coordenada de [x]: '))
y = float(input('Digite a coordenada de [y]: '))
r = float(input('Digite o calor de [R]'))

distancia = r**2+(x**2+y**2)

print('A distâcia de origem é {0}'.format(distancia))

