from datetime import datetime

class Hoteis:
    def __init__(self, nome_hotel, classificacao, preco_semana, preco_final_semana):
        self.nome_hotel = nome_hotel
        self.classificacao = classificacao
        self.preco_semana = preco_semana
        self.preco_final_semana = preco_final_semana

    def calcula_estadia(self, tipo_cliente, ds, dfds,):
        if tipo_cliente == 'Rewards':
            tc = 1
        else:
            tc = 0

        valor = 0

        if ds != 0:
            valor += ds * self.preco_semana[tc]
        if dfds != 0:
            valor += dfds * self.preco_final_semana[tc]

        #print(valor, self.classificacao, self.nome_hotel)
        return valor, self.classificacao, self.nome_hotel

'''
class melhor_reserva:
    def __init__(self, lista_hoteis):
        self.lista_hoteis = lista_hoteis

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

        Hoteis.calcula_estadia(tipo_cliente, qtd_dias_semana, qtd_dias_fds)
        #valor, self.classificacao, self.nome_hotel

    def melhor_hotel(self, lista_hoteis, tipo_cliente, dias_semana, dias_fds):
        valores = []
        for x in lista_hoteis:
            valores.append(x.calcula_estadia(tipo_cliente, dias_semana, dias_fds))

        menor_valor = 1000

        for x in valores:
            if menor_valor > x[0]:  # encontrando o menor valor
                menor_valor = x[0]
                melhor_hotel = x[2]
                classificacao = x[1]

            elif menor_valor == x[0] and classificacao < x[1]:
                melhor_hotel = x[2]
                classificacao = x[1]

        print(menor_valor, melhor_hotel, classificacao)
'''


