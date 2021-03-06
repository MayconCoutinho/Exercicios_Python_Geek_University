# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
# porcionalmente ao valor que cada deu para realização da aposta. Faça um programa 
# que leia quando cada apostador investiu, o valor do prêmio, e imprima quando cada 
# um ganharia do prêmio com base no valor investido

jogador_1 = int(input('Digite o valor que foi realizado apostar: '))
jogador_2 = int(input('Digite o valor que foi realizado apostar: '))
jogador_3 = int(input('Digite o valor que foi realizado apostar: '))
premio = int(input('Digite o valor do prêmio: '))

porcentagem = jogador_1+jogador_2+jogador_3
porcentagem_jogador_1 = jogador_1/porcentagem
porcentagem_jogador_2 = jogador_2/porcentagem
porcentagem_jogador_3 = jogador_3/porcentagem

p1 = porcentagem_jogador_1*premio
p2 = porcentagem_jogador_2*premio
p3 = porcentagem_jogador_3*premio

print('''

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

O prêmio Total é de R${3:.2f} 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
O jogador 1º apostou R${4:.2f} e receberá R${0:.2f} com {7:.2f}% do ganho.
O jogador 2º apostou R${5:.2f} e receberá R${1:.2f} com {8:.2f}% do ganho.
O jogador 3º apostou R${6:.2f} e receberá R${2:.2f} com {9:.2f}% do ganho.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''.format(p1,p2,p3,premio,jogador_1,jogador_2,jogador_3,porcentagem_jogador_1,porcentagem_jogador_2,porcentagem_jogador_3))