from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Column, Integer, String, Date

class Conexao:
    def __init__(self):
        self.user = "root"
        self.psw  = "1234"
        self.host = "localhost"
        self.port = "3306"

    def retornar_engine(self, basedados):
        connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
            self.user,
            self.psw,
            self.host,
            self.port,
            basedados
        )
        return create_engine(connection_string, echo=False) # echo = True, ativa debug

    def conectar(self, engine):
        Session = sessionmaker(bind=engine)
        return Session()

    def drop_and_create_all_table(self, engine):
        meta = MetaData()
        
        # Carrega todas as tabelas disponiveis na conexão e todas suas definições
        meta.reflect(engine)

        print("Deletando todas as tabelas...")
        meta.drop_all(engine)
        
        print("Adicionando todas as tabelas...")
        meta.create_all(engine)

    def truncate_table(self, engine, table):
        meta = MetaData()
        
        # Carrega todas as tabelas disponiveis na conexão e todas suas definições
        meta.reflect(engine)
        
        table = meta.tables[table]
        print(table.delete())
        engine.execute(table.delete())
        
    def truncate_all_tables(self, engine):
        meta = MetaData()
        
        # Carrega todas as tabelas disponiveis na conexão e todas suas definições
        meta.reflect(engine)
        
        for table in reversed(meta.sorted_tables):
            print (table.delete())
            engine.execute(table.delete())

# Modelos do pesquisados
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PesqMain(Base):
    __tablename__ = 'pesq_main'

    id       = Column(Integer, primary_key=True)
    id_grupo = Column(Integer)
    codigo   = Column(String(50))
    status   = Column(String(20))
    oculto   = Column(Integer)
    nome     = Column(String(150))
    sexo     = Column(String(1))
    cpf      = Column(String(15))
    cargo    = Column(String(50))

    def __init__(self, id, nome, codigo, status, sexo, cpf, cargo):
        self.id     = id
        self.oculto = 0
        self.nome   = nome
        self.codigo = codigo
        self.status = status
        self.sexo   = sexo
        self.cpf    = cpf
        self.cargo  = cargo

    def __repr__(self):
        return "<PesqMain(%s, %s, %s, %s)>" % (
            self.nome, self.codigo, self.status, self.sexo)

# Modelos do Employees (Dados a serem enviados)
class Employees(Base):
    __tablename__ = 'employees'

    emp_no     = Column(Integer, primary_key=True)
    birth_date = Column(Date)
    first_name = Column(String(14))
    last_name  = Column(String(16))
    gender     = Column(String(1))
    hire_date  = Column(Date)

    def __init__(self, first_name, last_name, birth_date, gender, hire_date):
        self.first_name = first_name
        self.last_name  = last_name
        self.birth_date = birth_date
        self.gender     = gender
        self.hire_date  = hire_date

    def __repr__(self):
        return "<Employees(%s, %s, %s, %s)>" % (
            self.first_name, self.last_name, self.birth_date, self.gender)

conexao = Conexao()
engine_sdd = conexao.retornar_engine('sdd_apres')
connection_sdd = conexao.conectar(engine_sdd)
#conexao.truncate_table(engine_sdd, 'pesq_main')
conexao.truncate_all_tables(engine_sdd)

engine_emp = conexao.retornar_engine('employees')
connection_emp = conexao.conectar(engine_emp)

print("Lendo employees...")
max = 5
employees = connection_emp.query(Employees).limit(max).all()
#employees = connection_emp.query(Employees).filter_by(id=1).first()

print("Adicionando registros...")
for emp in employees:
    novo_pesq_main = PesqMain(emp.emp_no, emp.first_name + " "+ emp.last_name, None, 'preenchido', emp.gender, '', '')
    connection_sdd.add(novo_pesq_main)
    connection_sdd.commit()
    # print("Registro %s adicionado" % emp.emp_no)

print("Registros adicionados")
pesq = connection_sdd.query(PesqMain).all()
print(pesq)
