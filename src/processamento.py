from datetime import datetime

# entrada = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
def processa_entrada(entrada):
    tipo_cliente = entrada.split(':')[0]  # (regular ou reward)
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

#print(valor, self.classificacao, self.nome_hotel)

def encontra_melhor_hotel(hoteis):
    global melhor_hotel, classificacao
    menor_valor = 1000

    for x in hoteis:
        if menor_valor > x[0]:  # encontrando o menor valor
            menor_valor = x[0]
            melhor_hotel = x[2]
            classificacao = x[1]

        elif menor_valor == x[0] and classificacao < x[1]:
            melhor_hotel = x[2]
            classificacao = x[1]

    #print(menor_valor, melhor_hotel, classificacao)
    return melhor_hotel