class AvaliacaoEstandeRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, avaliacao):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO avaliacao_estande (nota_apresentacao, nota_ideia, nota_experiencia, estande_id)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                avaliacao.nota_apresentacao,
                avaliacao.nota_ideia,
                avaliacao.nota_experiencia,
                avaliacao.estande_id
            ))
        self.conn.commit()