class EventoRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, evento):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO evento (nome, data_inicial, data_final, imagem, descricao, cep, rua, bairro, cidade, numero, complemento)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                evento.nome,
                evento.data_inicial,
                evento.data_final,
                evento.imagem,
                evento.descricao,
                evento.cep,
                evento.rua,
                evento.bairro,
                evento.cidade,
                evento.numero,
                evento.complemento
            ))
        self.conn.commit()

    def listar_todos(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM evento")
            return cursor.fetchall()

    def atualizar(self, evento):
        with self.conn.cursor() as cursor:
            sql = """
                UPDATE evento SET nome = %s, data_inicial = %s, data_final = %s, imagem = %s, descricao = %s, cep = %s, rua = %s, bairro = %s, cidade = %s, numero = %s, complemento = %s
                WHERE id = %s
            """
            cursor.execute(sql, (
                evento.nome,
                evento.data_inicial,
                evento.data_final,
                evento.imagem,
                evento.descricao,
                evento.cep,
                evento.rua,
                evento.bairro,
                evento.cidade,
                evento.numero,
                evento.complemento,
                evento.id
            ))
        self.conn.commit()

    def deletar(self, evento_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM evento WHERE id = %s"
            cursor.execute(sql, (evento_id,))
        self.conn.commit()
