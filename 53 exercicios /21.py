# Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
# de conversão é; K = L * 0,45 , sendo K a massa em quilogramas e L a massa em libras.



L =  int(input('Digite o valor de massa em libras para converte em quilogramas: '))
K = L*0.45
print('{0} libras = {1} quilograma '.format(L,K))