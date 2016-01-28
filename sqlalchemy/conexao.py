from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Conexao:

    def sessao(self):

        connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
            "root",
            "1234",
            "localhost",
            "3308",
            "sdd_apres"
        )

        # echo = True, ativa debug
        engine = create_engine(connection_string, echo=False)
        Session = sessionmaker(bind=engine)

        return Session()