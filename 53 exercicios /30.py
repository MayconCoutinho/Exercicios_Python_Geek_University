# Leia um valor em real e a cotação do dólar. Em seguida, emprima o valor correspondente
# em dólares.


real = float(input('Digite em real para converte em dólar: '))
valor_dola = float(input('Digite o valor do dola atual: '))
dola = (1/valor_dola)*real
print('{0} real = {2:.2f} dólar valor do dólar({1})'.format(real,valor_dola,dola))