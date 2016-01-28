from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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

    def __init__(self, nome, codigo, status, sexo, cpf, cargo):
        self.nome   = nome
        self.codigo = codigo
        self.status = status
        self.sexo   = sexo
        self.cpf    = cpf
        self.cargo  = cargo

    def __repr__(self):
        return "<pesq_main(%s, %s, %s, %s)>" % (
            self.nome, self.codigo, self.status, self.sexo)