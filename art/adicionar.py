from conexao import Conexao
from modelos import DecMain, DecEixoX, DecEixoY, DecEixoYPesq
from datetime import date

conexao = Conexao()
conexao.user = "root"
conexao.psw  = "1234"
conexao.host = "localhost"
conexao.port = "3306"

base_dados_exemplo = 'employees'
adicionar_na_base_dados = 'sdd_apres'

add_quantos_registros = 100 # `None` para todos os registros
ver_registros_add     = False