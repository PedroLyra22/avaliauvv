class EstandeRepository:
    def __init__(self, conn):
        self.conn = conn

    def inserir(self, estande):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO estande (nome, tema, imagem, descricao, evento_id)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                estande.nome,
                estande.tema,
                estande.imagem,
                estande.descricao,
                estande.evento_id
            ))
        self.conn.commit()

    def listar_todos(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM estande")
            return cursor.fetchall()

    def atualizar(self, estande):
        with self.conn.cursor() as cursor:
            sql = """
                UPDATE estande SET nome = %s, tema = %s, imagem = %s, descricao = %s, evento_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (
                estande.nome,
                estande.tema,
                estande.imagem,
                estande.descricao,
                estande.evento_id,
                estande.id
            ))
        self.conn.commit()

    def deletar(self, estande_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM estande WHERE id = %s"
            cursor.execute(sql, (estande_id,))
        self.conn.commit()
