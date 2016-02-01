Popular database teste com SQLAlchemy
===

Instalação
---

Clone o projeto localmente.

    $ git clone https://github.com/kenji-tabata/popular-db.git

Instale o VirtualEnv no projeto.

    $ virtualenv popular-db

Ative o VirtualEnv.

    $ source bin/activate

Instale os módulos SqlAlchemy e PyMySQL.

    $ pip install sqlalchemy
    $ pip install pymysql

Crie a base de dados do projeto no MySQL para testes, se necessário.

    $ mysql -h localhost -u root -p
    > CREATE DATABASE nome-da-database



Adicionando base de dados fictícia para testes
---

Clone o projeto `test_db` localmente.

    $ git clone https://github.com/datacharmer/test_db.git

Adicione no MySQL a base de dados `employees` do projeto `test_db`.

    $ mysql -h localhost -u root -p < employees.sql



Executando o script
---

No arquivo `pesquisados/adicionar.py` altere os dados da conexão do usuário do Mysql

    conexao.user = "seu-usuario"
    conexao.psw  = "sua-senha"
    conexao.host = "seu-endereço-de-host"
    conexao.port = "porta-do-mysql"

Altere o nome da base de dados para onde os dados serão adicionados

    adicionar_na_base_dados = "nome-da-base-de-dados"

Altere a quantidade de registros que serão adicionados

    add_quantos_registros = 100

Caso queira ver o log dos registros sendo adicionados altere para True a variável `ver_registros_add`.

    ver_registros_add = True

Para executar o script...

    $ python pesquisados/adicionar.py