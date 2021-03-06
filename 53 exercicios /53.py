# Faça um programa para ler as dimensões de um terreno (comprimento c e largura l).
# bem como o preço do metro de tela p. Imprimao custo para cercar este mesmo terreno 
# com tela.

tela = int(input('Digite o preço da tela em metros: '))
c = int(input('Digite o valor de [C] (comprimento): '))
l = int(input('Digite o valor de [l] (largura: )'))

comprimento = c*l
comprimento_de_tela = comprimento/4
custo = (comprimento/4)*tela
print('O comprimento do terreno é de {0}m².Para cerca-lo precisará de {2}m² de tela, que custará R${1:.2f}.'.format(comprimento,custo,comprimento_de_tela))