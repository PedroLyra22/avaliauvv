import pymysql.cursors

class DB:
    def __init__(self, host='localhost', user='root', password='', database='notalise'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor,
            port=3306
        )

    def fechar_conexao(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def get_conn(self):
        if not self.connection:
            self.conectar()
        return self.connection