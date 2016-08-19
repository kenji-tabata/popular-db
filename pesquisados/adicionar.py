from conexao import Conexao
from modelos import PesqMain, PesqComple, PesqPerf, Employees
from datetime import date
import random

# Dados...
conexao = Conexao()
conexao.user = "root"
conexao.psw  = "1234"
conexao.host = "localhost"
conexao.port = "3306"

base_dados_exemplo      = 'employees'
adicionar_na_base_dados = 'sdd_dom_apres'
ver_registros_add       = False
remover_add_tabelas     = False

# Adiciona a partir do registro 11001, remove todos os registros anteriores
adicionar_do_inicio = True
add_quantos_registros = 20 # `None` para todos os registros

# Adiciona a partir de um determinado intervalo, ideal para manter os regitros atuais
adicionar_entre_os_ids = False
id_inicial  = 1
id_final    = 20

def retornar_cpf():
    return str(random.randint(100, 999)) + "." + str(random.randint(100, 999)) + "." + str(random.randint(100, 999)) + "-" + str(random.randint(10, 99))

def retornar_valor(alternativas):
    alternativa = random.randint(1, 82)
    if alternativa not in alternativas:
        return alternativa
    return retornar_valor(alternativas)

def retornar_alternativas():
    alternativas = []
    limite = random.randint(11, 82)
    for alt in range(limite):
        alternativas.append(retornar_valor(alternativas))

    alternativas = str(sorted(alternativas))
    return alternativas.replace("[","").replace("]","")

#
# Executando conexões...
#
print("Conectando as base de dados...")
# Define a base de dados de exemplo
engine_employees = conexao.retornar_engine(base_dados_exemplo)
# Conecta com a base de dados `employees`
conexao_employees = conexao.conectar(engine_employees)
print("Conectado a base de dados %s" % base_dados_exemplo)

# Qual base de dados que receberá os dados de exemplo
engine_sdd = conexao.retornar_engine(adicionar_na_base_dados)
# Conecta com a base de dados selecionada
conexao_sdd = conexao.conectar(engine_sdd)
print("Conectado a base de dados %s" % adicionar_na_base_dados)

#
# Removendo tabelas ou registros...
#
if remover_add_tabelas:
    print("Deletando e criando as tabelas...")
    conexao.deletar_criar_todas_tabelas(engine_sdd)
    print("Tabelas criadas...")

if adicionar_do_inicio:
    print("Removendo registros...")
    # Remove todos os registros de uma tabela
    conexao.limpar_tabela(engine_sdd, 'pesq_comple')
    conexao.limpar_tabela(engine_sdd, 'pesq_perf')
    conexao.limpar_tabela(engine_sdd, 'pesq_main')

# Remove todos os registros de todas as tabelas
# conexao.limpar_todas_tabelas(engine_sdd)
# print("Registros deletados...")

#
# Lendo registros de exemplo...
#
print("Lendo employees...")
if add_quantos_registros and adicionar_do_inicio:
    employees = conexao_employees.query(Employees).limit(add_quantos_registros).all()
elif adicionar_entre_os_ids:
    employees = conexao_employees.query(Employees).filter(Employees.emp_no.between(id_inicial, id_final))
else:
    employees = conexao_employees.query(Employees).all()
print("Employees carregado na memória...")

#
# Adicionando registros...
#
print("Adicionando registros...")
for emp in employees:
    # Adicionando registros do PesqMain
    novo_pesq_main = PesqMain(
        emp.emp_no, emp.first_name + " "+ emp.last_name, None, 'preenchido',
        emp.gender, retornar_cpf(), emp.titles.title
    )
    conexao_sdd.add(novo_pesq_main)
    conexao_sdd.commit()

    # Adicionando registros do PesqComple
    novo_pesq_comple = PesqComple(
        emp.emp_no, emp.birth_date, '', '', '', '', '', '', '', '', '', '', '', '', date.today()
    )
    conexao_sdd.add(novo_pesq_comple)
    conexao_sdd.commit()

    # Adicionando registros do PesqPerf
    novo_pesq_perf = PesqPerf(
        emp.emp_no, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, retornar_alternativas(), '', ''
    )
    conexao_sdd.add(novo_pesq_perf)
    conexao_sdd.commit()

    if ver_registros_add:
        print("Registro %s adicionado" % emp.emp_no)

print("Registros adicionados")
print("Concluído!")

#print("Visualizar registros adicionados...")
#pesq = conexao_sdd.query(PesqMain).all()
#print(pesq)

