# Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundo = int(input('Digite em segundos para obter horas,minutos e segundo: '))
print('''


{0} segundos é o mesmo que:

{2} horas
{1} minutos


'''.format(segundo,segundo/60,segundo/120))