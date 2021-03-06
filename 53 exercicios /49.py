# Faça um programa para leia o horário(hora,minuto e segundo) de inicío e a duração , em 
# segundos de uma experiência biológica. O programa deve resultar com o novo horário
# (hora,minuto e segundo) do termino da mesma.

duração = int(input('Digite o a duração do experimento em segundo: '))
print('Digite em horas o inicio do experimento nessa ordem (horas,minutos,segundos)')

horas = int(input('---> '))
minutos = int(input('---> '))
segundos = int(input('---> '))

segundos_duração = (duração/120)



acrescimo_minuto = duração/60 # Se for possitivo acima de 0 acresenta 1 minuto.



acrescimo_hora = duração/3600 # Se for possitivo acima de 0 acresenta 1 hora.


contador_hora = 0 
contador_minuto = 0
contador_segundo = 0

if acrescimo_hora > 59 :
    contador_hora = acrescimo_hora/60
elif acrescimo_hora < 60:
    contador_hora = acrescimo_hora

if (duração/60) >= 1:
    if acrescimo_minuto > 59:
        contador_minuto = acrescimo_minuto/60
    elif acrescimo_minuto > 0:
        contador_minuto = acrescimo_minuto


if segundos_duração > 59:
    contador_segundo = segundos_duração/60
elif segundos_duração >1:
    contador_segundo = segundos_duração 

if duração > 0 and duração < 60:
    contador_segundo = duração
    
zero_hora = ''
zero_minuto = ''
zero_segundo = ''

if contador_hora < 10:
    zero_hora = 0
if contador_minuto < 10:
    zero_minuto = 0
if contador_segundo < 10:
    zero_segundo = 0



print('''

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Segundos de duração: {9}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Horário de Início: {6}:{7}:{8}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Horário de Termino: {3}{0:.0f}:{4}{1:.0f}:{5}{2:.0f}

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



'''.format(contador_hora,contador_minuto,contador_segundo,zero_hora,zero_minuto,zero_segundo,horas,minutos,segundos,duração))






   




