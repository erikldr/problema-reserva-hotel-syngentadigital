# importando o modulo datetime que contem varias funções interessantes, porem utilizei somente a isoweekday()
from datetime import datetime


# Passo 1
def processa_entrada(input_str):
    # Essa função recebe uma string como entrada
    tipo_cliente = input_str.split(':')[0] # A primeira parte da string contem o tipo de cliente
    # A segunda parte contem as datas
    datas = []
    # Aqui cada data é processada e convertida individualmente, e também é adicionada a uma lista
    for x in input_str.split(':')[1].split(','):
        datas.append(datetime.strptime(x.split('(')[0].strip(), "%d%b%Y"))

    ''' 
    Com as datas devidamente prontas para o uso utilizo a função isoweekday 
    para verificar se a data é ou não dia de semana.
    Tendo essa informação sera mais facil fazer os calculos da estadia
    '''
    qtd_dias_semana = 0
    qtd_dias_fds = 0

    '''
    A função isoweekday retorna um inteiro de acordo com a data
        ex: 08-05-2022 (dia 8 = domingo então o retorno seria 7)
    segunda a sexta = 1 a 5
    sabado = 6
    e domingo = 7
    '''
    for x in datas:
        if x.isoweekday() >= 6:
            qtd_dias_fds += 1
        else:
            qtd_dias_semana += 1
    '''
    Retorno da função:
        tipo_cliente = uma string - ("Reward" ou "Regular")
        qtd_dias_semana = um int com a quantidade de dias da semana 
        qtd_dias_fds = um int com a quantidade de dias de final de semana
    ex: "Reward", 2, 1
    '''
    return tipo_cliente, qtd_dias_semana, qtd_dias_fds


# Passo 3
def encontra_melhor_hotel(hoteis):
    # Essa função recebe uma lista com as informações de cada hotel (valor, classificação e nome)
    global melhor_hotel, classificacao
    menor_valor = 100000

    # Iteração com todos os hoteis
    for x in hoteis:
        # Encontrando o melhor valor
        if menor_valor > x[0]:
            menor_valor = x[0]
            melhor_hotel = x[2]
            classificacao = x[1] # Salvando a classificação do hotel (talvez seja necessaria em caso de empate)

        # Caso existam dois hoteis concorrentes no valor precisamos retornar o hotel com a melhor classificação
        elif menor_valor == x[0] and classificacao < x[1]:
            melhor_hotel = x[2]
            classificacao = x[1]
    '''
    Retorno da função
        melhor_hotel = o nome do melhor hotel levando em consideração o menor preço e classificação
    '''
    return melhor_hotel
