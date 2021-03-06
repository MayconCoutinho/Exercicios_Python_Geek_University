# Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
# de conversão é: L = K/0,45 ,sendo K a massa em qulogramas e L a massa em livras.


K = int(input('Digite o valor em quilogramas para converte em libras: '))
L = K/0.45
print('{0} quilogramas = {1:.2f} libras'.format(K,L))

