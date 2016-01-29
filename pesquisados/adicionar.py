from conexao import Conexao
from modelos import PesqMain, Employees

# Dados...
conexao = Conexao()
conexao.user = "root"
conexao.psw  = "1234"
conexao.host = "localhost"
conexao.port = "3306"

base_dados_exemplo = 'employees'
adicionar_na_base_dados = 'sdd_apres'

add_quantos_registros = 5

#
# Executando conexões...
#
print("Conectando as base de dados...")
# Define a base de dados de exemplo
engine_emp = conexao.retornar_engine(base_dados_exemplo)
# Conecta com a base de dados `employees`
connection_emp = conexao.conectar(engine_emp)
print("Conectado a base de dados %s" % base_dados_exemplo)

# Qual base de dados que receberá os dados de exemplo 
engine_sdd = conexao.retornar_engine(adicionar_na_base_dados)
# Conecta com a base de dados selecionada
connection_sdd = conexao.conectar(engine_sdd)
print("Conectado a base de dados %s" % adicionar_na_base_dados)

#
# Removendo tabelas ou registros...
#
# print("Deletando e criando as tabelas...")
# conexao.deletar_criar_todas_tabelas(engine_sdd)
# print("Tabelas criadas...")

print("Removendo registros...")
# Remove todos os registros de uma tabela
# conexao.limpar_tabela(engine_sdd, 'pesq_main')

# Remove todos os registros de todas as tabelas
conexao.limpar_todas_tabelas(engine_sdd)
print("Registros deletados...")

#
# Lendo registros de exemplo...
#
print("Lendo employees...")
employees = connection_emp.query(Employees).limit(add_quantos_registros).all()
print("Employees carregado na memória...")

#
# Adicionando registros...
#
print("Adicionando registros...")
for emp in employees:
    novo_pesq_main = PesqMain(emp.emp_no, emp.first_name + " "+ emp.last_name, None, 'preenchido', emp.gender, '', '')
    connection_sdd.add(novo_pesq_main)
    connection_sdd.commit()
    # print("Registro %s adicionado" % emp.emp_no)

print("Registros adicionados")
print("Concluído!")

print("Visualizar registros adicionados...")
pesq = connection_sdd.query(PesqMain).all()
print(pesq)


