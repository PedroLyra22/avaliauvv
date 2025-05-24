class EventoRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, evento):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO evento (nome, data_inicial, data_final, imagem, descricao, cep, rua, bairro, cidade, numero, complemento, admin_user_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                evento.admin_user_id
            ))
        self.conn.commit()

    def listar_todos(self, admin_user_id):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM evento WHERE admin_user_id = %s"
            cursor.execute(sql, (admin_user_id,))
            return cursor.fetchall()

    def atualizar(self, evento):
        with self.conn.cursor() as cursor:
            sql = """
                UPDATE evento 
                SET nome = %s, data_inicial = %s, data_final = %s, imagem = %s, descricao = %s, cep = %s, rua = %s, bairro = %s, cidade = %s, numero = %s, complemento = %s
                WHERE id = %s AND admin_user_id = %s
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
                evento.id,
                evento.admin_user_id
            ))
        self.conn.commit()

    def deletar(self, evento_id, admin_user_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM evento WHERE id = %s AND admin_user_id = %s"
            cursor.execute(sql, (evento_id, admin_user_id))
        self.conn.commit()