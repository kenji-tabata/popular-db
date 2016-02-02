from conexao import Conexao
from modelos import DecEixoYPesq

conexao = Conexao()
conexao.user = "root"
conexao.psw  = "1234"
conexao.host = "localhost"
conexao.port = "3306"

# Qual base de dados?
adicionar_na_base_dados = 'sdd_testes'

# Qual o id do Dec
id_dec = 1

# Quais os ids dos itens do Dec
lista_id_itens = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ids dos três primeiros itens
id_dec_1_item = 1
id_dec_3_item = 3

# Ids dos três últimos itens
id_dec_7_item = 7
id_dec_9_item = 9

# Id do sexto último item
id_dec_4_item = 4

# Quais serão pontuados
lista_pesq_alvo = [11001] # 3
lista_pesq_3_primeiros = [11002] # 50
lista_pesq_3_ultimos = [10001, 10002, 10003] # 10
lista_pesq_6_ultimos = [11003, 11004] # 20

print("Conectando as base de dados...")
engine = conexao.retornar_engine(adicionar_na_base_dados)
conectar = conexao.conectar(engine)
print("Conectado a base de dados %s" % adicionar_na_base_dados)

print("Removendo registros...")
conexao.limpar_tabela(engine, 'dec_eixo_y_pesq')

print("Adicionando registros 100% aderente")
for id_pesq in lista_pesq_alvo:
    for id_item in lista_id_itens:
        pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 1)
        conectar.add(pontuacao)
        conectar.commit()

print("Adicionando registros com somente os 3 primeiros")
for id_pesq in lista_pesq_3_primeiros:
    for id_item in lista_id_itens:
        if id_item >= id_dec_1_item and id_item <= id_dec_3_item:
            pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 1)
            conectar.add(pontuacao)
            conectar.commit()
        else:
            pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 2)
            conectar.add(pontuacao)
            conectar.commit()

print("Adicionando registros com somente os 3 últimos")
for id_pesq in lista_pesq_3_ultimos:
    for id_item in lista_id_itens:
        if id_item >= id_dec_7_item and id_item <= id_dec_9_item:
            pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 1)
            conectar.add(pontuacao)
            conectar.commit()
        else:
            pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 2)
            conectar.add(pontuacao)
            conectar.commit()

print("Adicionando registros com somente os 6 últimos")
for id_pesq in lista_pesq_6_ultimos:
    for id_item in lista_id_itens:
        if id_item >= id_dec_4_item and id_item <= id_dec_9_item:
            pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 1)
            conectar.add(pontuacao)
            conectar.commit()
        else:
            pontuacao = DecEixoYPesq(id_dec, id_pesq, id_item, 2)
            conectar.add(pontuacao)
            conectar.commit()

