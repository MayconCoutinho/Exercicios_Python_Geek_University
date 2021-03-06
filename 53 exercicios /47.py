# Leia um número inteiro de 4 digitos(de 1000 a 9999) e imprima 1 digito por linha.


numero = str(input('Digite um número inteiro de 4 digitos ex(1000 a 9999): '))
numero_lista = list(numero) 
contador = len(numero_lista)

for r in range(0,contador):
    print(numero_lista[(r)])