from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

Base = declarative_base()

class DecMain(Base):
    __tablename__ = 'dec_main'

    id      = Column(Integer, primary_key=True)
    nome    = Column(String(100), nullable=False)
    corte_y = Column(Integer, nullable=True)
    corte_x = Column(Integer, nullable=True)

    def __init__(self, nome, corte_y, corte_x):
        self.nome    = nome
        self.corte_y = corte_y
        self.corte_x = corte_x

    def __repr__(self):
        return "<DecMain(%s)>" % (self.nome)

class DecEixoX(Base):
    __tablename__ = 'dec_eixo_x'

    id              = Column(Integer, primary_key=True)
    id_dec          = Column(Integer, nullable=False)
    id_fator        = Column(Integer, nullable=False)
    valor_1         = Column(Boolean, nullable=True)
    valor_2         = Column(Boolean, nullable=True)
    valor_3         = Column(Boolean, nullable=True)
    valor_4         = Column(Boolean, nullable=True)
    valor_5         = Column(Boolean, nullable=True)
    valor_escolhido = Column(Boolean, nullable=True)
    acoes           = Column(String(255), nullable=True)

    def __init__(self, id_dec, id_fator, valor_1, valor_2, valor_3, valor_4, valor_5, valor_escolhido, acoes):
        self.id_dec          = id_dec
        self.id_fator        = id_fator
        self.valor_1         = valor_1
        self.valor_2         = valor_2
        self.valor_3         = valor_3
        self.valor_4         = valor_4
        self.valor_5         = valor_5
        self.valor_escolhido = valor_escolhido
        self.acoes           = acoes

    def __repr__(self):
        return "<DecEixoX(%s)>" % (str(self.id_dec))

class DecEixoY(Base):
    __tablename__ = 'dec_eixo_y'

    id              = Column(Integer, primary_key=True)
    id_dec          = Column(Integer, nullable=False)
    item            = Column(String(200), nullable=False)
    sub_item_1      = Column(String(150), nullable=False)
    sub_item_2      = Column(String(150), nullable=False)
    sub_item_3      = Column(String(150), nullable=True)
    sub_item_4      = Column(String(150), nullable=True)
    sub_item_5      = Column(String(150), nullable=True)
    valor_1         = Column(Boolean, nullable=True)
    valor_2         = Column(Boolean, nullable=True)
    valor_3         = Column(Boolean, nullable=True)
    valor_4         = Column(Boolean, nullable=True)
    valor_5         = Column(Boolean, nullable=True)
    valor_escolhido = Column(Boolean, nullable=True)
    acoes           = Column(String(255), nullable=True)

    def __init__(self, id_dec, item, sub_item_1, sub_item_2, sub_item_3, sub_item_4, sub_item_5,
        valor_1, valor_2, valor_3, valor_4, valor_5, valor_escolhido, acoes):
        self.id_dec          = id_dec
        self.item            = item
        self.sub_item_1      = sub_item_1
        self.sub_item_2      = sub_item_2
        self.sub_item_3      = sub_item_3
        self.sub_item_4      = sub_item_4
        self.sub_item_5      = sub_item_5
        self.valor_1         = valor_1
        self.valor_2         = valor_2
        self.valor_3         = valor_3
        self.valor_4         = valor_4
        self.valor_5         = valor_5
        self.valor_escolhido = valor_escolhido
        self.acoes           = acoes

    def __repr__(self):
        return "<DecEixoY(%s)>" % (self.item)

class DecEixoYPesq(Base):
    __tablename__ = 'dec_eixo_y_pesq'

    id_dec  = Column(Integer, primary_key=True)
    id_pesq = Column(Integer, primary_key=True)
    id_item = Column(Integer, primary_key=True)
    gap     = Column(Boolean, nullable=False)

    def __init__(self, id_dec, id_pesq, id_item, gap):
        self.id_dec  = id_dec
        self.id_pesq = id_pesq
        self.id_item = id_item
        self.gap     = gap

    def __repr__(self):
        return "<DecEixoYPesq(%s, %s, %s, %s)>" % (self.id_dec, self.id_pesq, self.id_item, self.gap)
