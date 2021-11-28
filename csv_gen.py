import csv
import names
import random
from random import randint
from datetime import datetime
from nltk.corpus import wordnet as wn

food = wn.synset('food.n.02')
food_list = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

def random_termo(termo):
    r = randint(0,100)
    if(r%25 == 0):
        if type(termo) == str:
            return ''
        if type(termo) == int:
            return 0
        if type(termo) == float:
            return 0.0
        if type(termo) == datetime:
            return datetime(1, 1, 1)
    else:
        return termo

def povoar_restaurante():

    def cnpj(punctuation = True):
        n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
        v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
        # calcula dígito 1 e acrescenta ao total
        s = sum(x * y for x, y in zip(reversed(n), v))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)
        # idem para o dígito 2
        s = sum(x * y for x, y in zip(reversed(n), v))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)
        if punctuation:
            return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
        else:
            return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)
    
    global linha

    linha = []

    def telefone():
        return str(randint(10, 99))+str(randint(1000,99999))+str(randint(1000,9999))

    def sufixo_loja():
        s = [' SA.', ' ME.', ' LTDA.', ' INC.', ]
        return s[randint(0,len(s)-1)]

    def prefixo_end():
        r = ['Rua ', 'Avenida ', 'Praça ', 'Rodovia ', 'Sitio ', 'Vila ', 'Condomínio ', 'Parque ']
        return r[randint(0, len(r)-1)]

    for _ in range(10000):
        linha.append([
            cnpj(), 
            random_termo(str(names.get_last_name().upper()+sufixo_loja())), 
            random_termo(randint(0,100)/10), 
            random_termo(str(randint(10000,99999))+'-'+str(randint(100,999))), 
            random_termo(randint(1,9999)),
            random_termo(str(prefixo_end()+names.get_last_name().capitalize())), 
            random_termo(telefone())
        ])

    with open('./restaurantes.csv', 'w') as arqcsv:
        # w.writerow('cnpj', 'nome_loja', 'cep', 'numero', 'endereco', 'telefone')
        w = csv.writer(arqcsv, delimiter=',', quotechar='|')
        for l in linha:
            w.writerow(l)

# povoar_restaurante()

def povoar_pratos():

    linha = []
    for i in range(randint(7500, 15000)):
        linha.append([
            i, #prato_id
            randint(199, 50000)/100, #preco
            randint(0, 50), #categoria
            food_list[randint(0, len(food_list) -1)] # nome_prato
        ])

    with open('./pratos.csv', 'w') as arqcsv:
        w = csv.writer(arqcsv, delimiter=',', quotechar='|')
        # w.writerow(['prato_id', 'preco', 'categoria', 'nome_prato'])
        for l in linha:
            w.writerow(l)

# povoar_pratos()

def povoar_cupons():
    # data_inicial = datetime.fromtimestamp(1000000000.000000)
    # aproximadamente 6 dias e 22hrs depois 
    # data_final   = datetime.fromtimestamp(1000599999.000000)

    linha = []

    for i in range(randint(75000, 150000)):
        ano_aleatorio = str(randint(1000,1600))
        dia_aleatorio = str(randint(100000,599999))
        data_inicial  = datetime.fromtimestamp(float(ano_aleatorio + dia_aleatorio + '.000000'))
        data_final    = datetime.fromtimestamp(float(ano_aleatorio + str(randint(int(dia_aleatorio),599999)) + '.000000'))

        linha.append([
            data_inicial, data_final, randint(1,25)/100
        ])

    with open('./cupons.csv', 'w') as arqcsv:
        w = csv.writer(arqcsv, delimiter=',', quotechar='|')
        # w.writerow(['data_inicial', 'data_final', 'desconto'])
        for l in linha:
            w.writerow(l)

# povoar_cupons()

def povoar_pessoas():

    def cpf(punctuation = True):
        n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
        v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
        # calcula dígito 1 e acrescenta ao total
        s = sum(x * y for x, y in zip(reversed(n), v))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)
        # idem para o dígito 2
        s = sum(x * y for x, y in zip(reversed(n), v))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)
        if punctuation:
            return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n[:11])
        else:
            return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)

    def sufixo_email():
        r = ['@outlook.com', '@yahoo.com', '@aol.com', '@protonmail.com' '@icloud.com', '@gmail.com']
        return r[randint(0, len(r)-1)]

    def prefixo_end():
        r = ['Rua ', 'Avenida ', 'Praça ', 'Rodovia ', 'Sitio ', 'Vila ', 'Condomínio ', 'Parque ']
        return r[randint(0, len(r)-1)]

    def telefone():
        return str(randint(10, 99))+str(randint(1000,99999))+str(randint(1000,9999))

    def sexo():
        s = ['m', 'f', 'o']
        return s[randint(0, len(s) - 1)]

    linha = []

    for _ in range(100000):
        data_nascimento = datetime(1920, 1, 1) + (datetime.now() - datetime(1920, 1, 1)) * random.random()
        linha.append([
            random_termo(names.get_full_name()), #nome
            cpf(), 
            random_termo(telefone()), #telefone
            random_termo(names.get_first_name() + '.' + names.get_last_name() + sufixo_email()),
            random_termo(str(randint(10000,99999))+'-'+str(randint(100,999))),  #cep
            random_termo(str(prefixo_end()+names.get_last_name().capitalize())), #endereco
            random_termo(randint(1,9999)), #numero
            random_termo(data_nascimento), #data de nascimento
            random_termo(sexo())
        ])

    with open('./pessoas.csv', 'w') as arqcsv:
        w = csv.writer(arqcsv, delimiter=',', quotechar='|')
        # w.writerow(['prato_id', 'preco', 'categoria', 'nome_prato'])
        for l in linha:
            w.writerow(l)

# povoar_pessoas()

def povoar_pedido():

    def forma_pagamento():
        fp = ['Credit card', 'Debit card', 'Money', 'Food voucher', 'Bank transfer']
        return fp[randint(0, len(fp)-1)]

    linha = []

    def cpf(punctuation = True):
        n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
        v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
        # calcula dígito 1 e acrescenta ao total
        s = sum(x * y for x, y in zip(reversed(n), v))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)
        # idem para o dígito 2
        s = sum(x * y for x, y in zip(reversed(n), v))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)
        if punctuation:
            return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n[:11])
        else:
            return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)

    entregadores = [cpf() for x in range(1000)]

    for p in range(10000):
        ano_aleatorio = str(randint(10000,16000))
        dia_aleatorio = str(randint(10000,12000))
        data_inicial  = datetime.fromtimestamp(float(ano_aleatorio + dia_aleatorio + '.000000'))
        data_final    = datetime.fromtimestamp(float(ano_aleatorio + str(randint(int(dia_aleatorio),599999)) + '.000000'))
        linha.append([
            forma_pagamento(), # forma_pagamento
            data_inicial, # horario_inicio
            data_final, # horario_final
            entregadores[randint(0, len(entregadores)-1)], # entregador
            random_termo(randint(-1, 95153)), # id_cupom
            randint(0,9999), # id_restaurante
            random_termo(randint(0, 99999)), # id_cliente
            p, # id_pedido
            random_termo(randint(0, 7784)) # id_prato
        ])

    with open('./pedidos.csv', 'w') as arqcsv:
        w = csv.writer(arqcsv, delimiter=',', quotechar='|')
        # w.writerow(['prato_id', 'preco', 'categoria', 'nome_prato'])
        for l in linha:
            w.writerow(l)

# povoar_pedido()