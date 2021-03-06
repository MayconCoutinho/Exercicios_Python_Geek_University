# Faça um programa que leia um número inteiro positivo de três dígitos(de 100 a 999).
# Gere outro número formado pelos dígitos incertidos do número lido. Exemplo:
# -----> NúmeroLido = 123
# -----> NúmeroGerado = 321


numero = str(input('Digite um numero inteiro de 3 digitos ex(100 a 999): '))
numero_invertido = numero[::-1]
print(numero_invertido)