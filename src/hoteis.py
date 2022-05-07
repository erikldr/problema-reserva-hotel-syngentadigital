class Hoteis:
    def __init__(self, nome_hotel, classificacao, preco_semana, preco_final_semana):
        self.nome_hotel = nome_hotel
        self.classificacao = classificacao
        self.preco_semana = preco_semana
        self.preco_final_semana = preco_final_semana

    def calcula_estadia(self, tipo_cliente, ds, dfds):
        if tipo_cliente == 'Rewards':
            tc = 1
        else:
            tc = 0

        valor = 0

        if ds != 0:
            valor += ds * self.preco_semana[tc]
        if dfds != 0:
            valor += dfds * self.preco_final_semana[tc]

        return valor, self.classificacao, self.nome_hotel




