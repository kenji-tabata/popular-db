from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

# Modelos do pesquisados
class PesqMain(Base):
    __tablename__ = 'pesq_main'

    id       = Column(Integer, primary_key=True)
    id_grupo = Column(Integer, nullable=True)
    codigo   = Column(String(50), nullable=True)
    status   = Column(String(20), nullable=False)
    oculto   = Column(Integer, nullable=False)
    nome     = Column(String(150), nullable=False)
    sexo     = Column(String(1), nullable=False)
    cpf      = Column(String(15), nullable=False)
    cargo    = Column(String(50), nullable=False)

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
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name  = Column(String(16), nullable=False)
    gender     = Column(String(1), nullable=False)
    hire_date  = Column(Date, nullable=False)

    # One-to-many
    # titles = relationship("Titles", backref=backref('employees', order_by=emp_no))

    # One-to_one
    title = relationship("Titles", uselist=False, back_populates="employee")

    def __init__(self, first_name, last_name, birth_date, gender, hire_date):
        self.first_name = first_name
        self.last_name  = last_name
        self.birth_date = birth_date
        self.gender     = gender
        self.hire_date  = hire_date

    def __repr__(self):
        return "<Employees(%s, %s, %s, %s)>" % (
            self.first_name, self.last_name, self.birth_date, self.gender)

class Titles(Base):
    __tablename__ = 'titles'

    emp_no    = Column(Integer, ForeignKey("employees.emp_no"), primary_key=True)
    title     = Column(String(50), nullable=False)
    from_date = Column(Date, nullable=False)
    to_date   = Column(Date, nullable=True)

    employee = relationship("Employees", back_populates="title")

    def __init__(self, title, from_date, to_date):
        self.title     = title
        self.from_date = from_date
        self.to_date   = to_date

    def __repr__(self):
        return "<Titles(%s)>" % (
            self.title)