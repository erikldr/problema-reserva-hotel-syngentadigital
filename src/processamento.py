from datetime import datetime


# Primeiro passo
# Extração dos dados da string atravez de splits
def processa_entrada(entrada):
    tipo_cliente = entrada.split(':')[0]
    datas = []
    for x in entrada.split(':')[1].split(','):
        datas.append(datetime.strptime(x.split('(')[0].strip(), "%d%b%Y"))

    qtd_dias_semana = 0
    qtd_dias_fds = 0
    for x in datas:
        if x.isoweekday() >= 6:
            qtd_dias_fds += 1
        else:
            qtd_dias_semana += 1
    return tipo_cliente, qtd_dias_semana, qtd_dias_fds


# Terceiro passo
def encontra_melhor_hotel(hoteis):
    global melhor_hotel, classificacao
    menor_valor = 100000

    for x in hoteis:
        if menor_valor > x[0]:
            menor_valor = x[0]
            melhor_hotel = x[2]
            classificacao = x[1]

        elif menor_valor == x[0] and classificacao < x[1]:
            melhor_hotel = x[2]
            classificacao = x[1]

    return melhor_hotel
