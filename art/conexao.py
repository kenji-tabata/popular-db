from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class Conexao:
    def __init__(self):
        self.user = ""
        self.psw  = ""
        self.host = ""
        self.port = ""

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

    def deletar_criar_todas_tabelas(self, engine):
        meta = MetaData()

        # Carrega todas as tabelas disponiveis na conexão e todas suas definições
        meta.reflect(engine)

        print("Deletando todas as tabelas...")
        meta.drop_all(engine)

        print("Adicionando todas as tabelas...")
        meta.create_all(engine)

    def limpar_tabela(self, engine, table):
        meta = MetaData()

        # Carrega todas as tabelas disponiveis na conexão e todas suas definições
        meta.reflect(engine)

        table = meta.tables[table]
        print(table.delete())
        engine.execute(table.delete())

    def limpar_todas_tabelas(self, engine):
        meta = MetaData()

        # Carrega todas as tabelas disponiveis na conexão e todas suas definições
        meta.reflect(engine)

        for table in reversed(meta.sorted_tables):
            print (table.delete())
            engine.execute(table.delete())

