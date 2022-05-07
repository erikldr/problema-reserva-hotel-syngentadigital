from src.hoteis import Hoteis
import src.processamento as processamento

Lakewood = Hoteis('Lakewood', 3, [110, 80], [90, 80])
Bridgewood = Hoteis('Bridgewood', 4, [160, 110], [60, 50])
Ridgewood = Hoteis('Ridgewood', 5, [220, 100], [150, 40])
lista_hoteis = [Lakewood, Bridgewood, Ridgewood]

def get_cheapest_hotel(entrada):   #DO NOT change the function's name
    tipo_hotel, qtd_dia_semana, qtd_dia_final_semana = processamento.processa_entrada(entrada)

    preco_por_cada_hotei = [] # aqui eu salvo para cada hotel o valor a classificacao e nome_hotel
    for x in lista_hoteis:
        preco_por_cada_hotei.append(x.calcula_estadia(tipo_hotel, qtd_dia_semana, qtd_dia_final_semana))
    # depois ja ter o valor de cada hotel eu so preciso encontrar qual [e o melhor
    cheapest_hotel = processamento.encontra_melhor_hotel(preco_por_cada_hotei)
    print(preco_por_cada_hotei)
    print(cheapest_hotel)
    return cheapest_hotel

entrada1 = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
entrada2 = 'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'
entrada3 = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'

get_cheapest_hotel(entrada3)




