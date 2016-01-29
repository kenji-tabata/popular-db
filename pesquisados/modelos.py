from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Modelos do pesquisados
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