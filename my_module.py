from hoteis import Hoteis
from datetime import datetime

Lakewood = Hoteis('Lakewood', 3, [110, 80], [90, 80])
Bridgewood = Hoteis('Bridgewood', 4, [160, 110], [60, 50])
Ridgewood = Hoteis('Ridgewood', 5, [220, 100], [150, 40])
lista_hoteis = [Lakewood, Bridgewood, Ridgewood]

def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"
    return cheapest_hotel

entrada1 = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
entrada2 = 'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'
entrada3 = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'


def processa_entrada(entrada):
    tipo_cliente = entrada.split(':')[0]  # (regular ou reward)
    datas = []
    for x in entrada.split(':')[1].split(','):
        datas.append(datetime.strptime(x.split('(')[0].strip(), "%d%b%Y"))
    return tipo_cliente, datas

tc, datas = processa_entrada(entrada3)

def conta_dias(datas):
    qtd_dias_semana = 0
    qtd_dias_fds = 0

    for x in datas:
        if x.isoweekday() >= 6:
            qtd_dias_fds += 1
        else:
            qtd_dias_semana += 1
    return qtd_dias_semana, qtd_dias_fds

ds, dfds = conta_dias(datas)

valores = []
for x in lista_hoteis:
    valores.append(x.calcula_estadia(tc, ds, dfds))

menor_valor = 1000

for x in valores:
    if menor_valor > x[0]: # encontrando o menor valor
        menor_valor = x[0]
        melhor_hotel = x[2]
        classificacao = x[1]

    elif menor_valor == x[0] and classificacao < x[1]:
        melhor_hotel = x[2]
        classificacao = x[1]

print(menor_valor, melhor_hotel, classificacao)

#print(melhor_hotel)

