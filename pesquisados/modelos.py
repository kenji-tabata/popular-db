from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Modelos do pesquisados
class PesqMain(Base):
    __tablename__ = 'pesq_main'

    id       = Column(Integer, primary_key=True)
    id_grupo = Column(Integer, nullable=True)
#    codigo   = Column(String(50), nullable=True) # Verificar se a tabela possui o campo código
    status   = Column(String(20), nullable=False)
    oculto   = Column(Boolean, nullable=False)
    nome     = Column(String(150), nullable=False)
    sexo     = Column(String(1), nullable=False)
    cpf      = Column(String(15), nullable=False)
    cargo    = Column(String(50), nullable=False)

    pesq_comple = relationship("PesqComple", uselist=False, back_populates="pesq_main")
    pesq_perf = relationship("PesqPerf", uselist=False, back_populates="pesq_main")

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

class PesqComple(Base):
    __tablename__ = "pesq_comple"

    id_pesq      = Column(Integer, ForeignKey("pesq_main.id"), primary_key=True)
    dt_nasc      = Column(Date, nullable=False)
    endereco     = Column(String(100), nullable=False)
    bairro       = Column(String(50), nullable=False)
    cidade       = Column(String(50), nullable=False)
    uf           = Column(String(2), nullable=False)
    cep          = Column(String(10), nullable=False)
    telefone_res = Column(String(20), nullable=False)
    telefone_cel = Column(String(20), nullable=False)
    telefone_com = Column(String(20), nullable=False)
    email        = Column(String(150), nullable=False)
    formacao     = Column(String(50), nullable=False)
    empresa      = Column(String(50), nullable=False)
    dt_adm       = Column(String(30), nullable=False)
    dt_preen     = Column(Date, nullable=False)

    pesq_main = relationship("PesqMain", back_populates="pesq_comple")

    def __init__(self, id_pesq, dt_nasc, end, bairro, cidade, uf, cep, tel_res, tel_cel, tel_com, email, formacao, empresa, dt_adm, dt_preen):
        self.id_pesq = id_pesq
        self.dt_nasc = dt_nasc
        self.endereco = end
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.telefone_res = tel_res
        self.telefone_cel = tel_cel
        self.telefone_com = tel_com
        self.email = email
        self.formacao = formacao
        self.empresa = empresa
        self.dt_adm = dt_adm
        self.dt_preen = dt_preen

    def __repr__(self):
        return "<PesqComple(%s, %s)>" % (
            str(self.id_pesq), self.dt_nasc)

class PesqPerf(Base):
    __tablename__ = "pesq_perf"

    id_pesq      = Column(Integer, ForeignKey("pesq_main.id"), primary_key=True)
    id_perf      = Column(Integer, nullable=True)
    base         = Column(String(9), nullable=True)
    lid          = Column(Integer, nullable=True)
    empr         = Column(Integer, nullable=True)
    com          = Column(Integer, nullable=True)
    arg          = Column(Integer, nullable=True)
    vel          = Column(Integer, nullable=True)
    prat         = Column(Integer, nullable=True)
    det          = Column(Integer, nullable=True)
    orga         = Column(Integer, nullable=True)
    cnor         = Column(Integer, nullable=True)
    perc         = Column(Integer, nullable=True)
    intu         = Column(Integer, nullable=True)
    crit         = Column(Integer, nullable=True)
    decir        = Column(Integer, nullable=True)
    cria         = Column(Integer, nullable=True)
    ener         = Column(Integer, nullable=True)
    alternativas = Column(Text, nullable=False)
    el           = Column(Text, nullable=True)
    sit          = Column(Text, nullable=True)

    pesq_main = relationship("PesqMain", back_populates="pesq_perf")

    def __init__(self, id_pesq, id_perf, base, lid, empr, com, arg, vel, prat, det, orga, cnor, perc, intu, crit, decir, cria, ener, alternativas, el, sit):
        self.id_pesq      = id_pesq
        self.id_perf      = id_perf
        self.base         = base
        self.lid          = lid
        self.empr         = empr
        self.com          = com
        self.arg          = arg
        self.vel          = vel
        self.prat         = prat
        self.det          = det
        self.orga         = orga
        self.cnor         = cnor
        self.perc         = perc
        self.intu         = intu
        self.crit         = crit
        self.decir        = decir
        self.cria         = cria
        self.ener         = ener
        self.alternativas = alternativas
        self.el           = el
        self.sit          = sit

    def __repr__(self):
        return "<PesqPerf(%s, %s)>" % (
            str(self.id_pesq), self.alternativas)

#from sqlalchemy.orm import backref

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
    titles = relationship("Titles", uselist=False, back_populates="employees")

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

    employees = relationship("Employees", back_populates="titles")

    def __init__(self, title, from_date, to_date):
        self.title     = title
        self.from_date = from_date
        self.to_date   = to_date

    def __repr__(self):
        return "<Titles(%s)>" % (
            self.title)