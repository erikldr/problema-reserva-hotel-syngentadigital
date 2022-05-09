# Importação dos modulos que foram criados em outros arquivos
# Para o pytest foi necessario colocar o caminho completo de cada um
from src.hoteis import Hoteis
import src.processamento as processamento

# Criando os hoteis e efinindo as caracteristicas de cada um
Lakewood = Hoteis('Lakewood', 3, [110, 80], [90, 80])
Bridgewood = Hoteis('Bridgewood', 4, [160, 110], [60, 50])
Ridgewood = Hoteis('Ridgewood', 5, [220, 100], [150, 40])

hoteis = [Lakewood, Bridgewood, Ridgewood]  # Uma lista com os 3 hoteis para faccilitar


def get_cheapest_hotel(entrada):
    # Essa é a função printipal, o ponto de partida, so deixei nela o que nao era interessante modularizar.

    # Passo 1 - chamando a função processa_entrada e salvando seu retorno nas variaves para utilização
    tipo_cliente, qtd_dia_semana, qtd_dia_final_semana = processamento.processa_entrada(entrada)

    info_hoteis = []  # uma lista contendo outras 3 listas (uma para cada hotel) contendo o valor, a classificação e o nome
    for x in hoteis:
        # Passo 2 - chamando a função calcula_estadia, ela fara os calculos para cada hotel
        info_hoteis.append(x.calcula_estadia(tipo_cliente, qtd_dia_semana, qtd_dia_final_semana))

    # Passo 3 - encontrando de fato qual é o melhor hotel de acordo com o valor e classificação
    cheapest_hotel = processamento.encontra_melhor_hotel(info_hoteis)

    '''
    Retorno da função:
        cheapest_hotel = uma string com o nome do hotel com o menor preço e maior classificação
    '''
    return cheapest_hotel

