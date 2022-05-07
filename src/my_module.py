from src.hoteis import Hoteis
import src.processamento as processamento

# Definindo as caracteristicas de cada hotel
Lakewood = Hoteis('Lakewood', 3, [110, 80], [90, 80])
Bridgewood = Hoteis('Bridgewood', 4, [160, 110], [60, 50])
Ridgewood = Hoteis('Ridgewood', 5, [220, 100], [150, 40])
hoteis = [Lakewood, Bridgewood, Ridgewood]


def get_cheapest_hotel(entrada):   #DO NOT change the function's name
    tipo_hotel, qtd_dia_semana, qtd_dia_final_semana = processamento.processa_entrada(entrada)
    info_hoteis = []
    for x in hoteis:
        info_hoteis.append(x.calcula_estadia(tipo_hotel, qtd_dia_semana, qtd_dia_final_semana))
    cheapest_hotel = processamento.encontra_melhor_hotel(info_hoteis)
    return cheapest_hotel

