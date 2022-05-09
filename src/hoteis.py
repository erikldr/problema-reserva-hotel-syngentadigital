'''
Visto que todos os hoteis tinham os mesmos atributos e uma função em comum
Criei a classe Hotel onde os atributos e a função foram definidos
'''
class Hoteis:
    def __init__(self, nome_hotel, classificacao, preco_semana, preco_final_semana):
        self.nome_hotel = nome_hotel
        self.classificacao = classificacao
        self.preco_semana = preco_semana
        self.preco_final_semana = preco_final_semana

    # Passo 2
    def calcula_estadia(self, tipo_cliente, ds, dfds):
        # Essa função recebe o tipo de cliente, a quantidade de dias da semana, e a quantidade de dias de final de semana

        # Na variavel tc eu apenas salvo de uma forma diferente o tipo de cliente (pequena conversão de string para int),
        # Com isso eu consigo acessar o preço para cada um de forma mais facil
        if tipo_cliente == 'Rewards':
            tc = 1
        else:
            tc = 0

        valor = 0  # Ao final essa variavel vai conter a soma total do valor da estadia para aquela entrada

        # Eu verifico se é diferente de 0 pois se uma entrada for apenas para dias de semana
        # eu nao preciso calcular final de semana e vice-versa
        if ds != 0:
            valor += ds * self.preco_semana[tc]
        if dfds != 0:
            valor += dfds * self.preco_final_semana[tc]
        '''
        Retorno da função:
            valor = o valor tota da estadia de acordo com as datas
            classificação = a classificação sera necessaria na ultima parte onde caso haja empate nos valores 
                            o hotel com a melhor classificação sera o escolhido
            nome_hotel = o nome do hotel 
        '''
        return valor, self.classificacao, self.nome_hotel




