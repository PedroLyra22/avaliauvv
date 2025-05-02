class AvaliacaoEventoRepository:
    def __init__(self, conn):
        self.conn = conn

    def inserir(self, avaliacao):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO avaliacao_evento (nota_equipe, nota_infraestrutura, nota_organizacao, nota_experiencia, imagem_avaliacao, evento_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                avaliacao.nota_equipe,
                avaliacao.nota_infraestrutura,
                avaliacao.nota_organizacao,
                avaliacao.nota_experiencia,
                avaliacao.imagem_avaliacao,
                avaliacao.evento_id
            ))
        self.conn.commit()