class EstandeRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, estande):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO estande (nome, tema, imagem, descricao, evento_id, admin_user_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                estande.nome,
                estande.tema,
                estande.imagem,
                estande.descricao,
                estande.evento_id,
                estande.admin_user_id
            ))
        self.conn.commit()

    def listar_todos(self, admin_user_id):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM estande WHERE admin_user_id = %s"
            cursor.execute(sql, (admin_user_id,))
            return cursor.fetchall()

    def atualizar(self, estande):
        with self.conn.cursor() as cursor:
            sql = """
                UPDATE estande 
                SET nome = %s, tema = %s, imagem = %s, descricao = %s, evento_id = %s
                WHERE id = %s AND admin_user_id = %s
            """
            cursor.execute(sql, (
                estande.nome,
                estande.tema,
                estande.imagem,
                estande.descricao,
                estande.evento_id,
                estande.id,
                estande.admin_user_id
            ))
        self.conn.commit()

    def deletar(self, estande_id, admin_user_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM estande WHERE id = %s AND admin_user_id = %s"
            cursor.execute(sql, (estande_id, admin_user_id))
        self.conn.commit()