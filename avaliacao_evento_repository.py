class AvaliacaoEventoRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, avaliacao):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO avaliacao_evento (nota_equipe, nota_infraestrutura, nota_organizacao, nota_experiencia, evento_id)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                avaliacao.nota_equipe,
                avaliacao.nota_infraestrutura,
                avaliacao.nota_organizacao,
                avaliacao.nota_experiencia,
                avaliacao.evento_id
            ))
        self.conn.commit()

    def media_por_evento(self, evento_id):
        with self.conn.cursor() as cursor:
            sql = """
                SELECT 
                    AVG(nota_equipe) AS media_nota_equipe,
                    AVG(nota_infraestrutura) AS media_nota_infraestrutura,
                    AVG(nota_organizacao) AS media_nota_organizacao,
                    AVG(nota_experiencia) AS media_nota_experiencia
                FROM avaliacao_evento
                WHERE evento_id = %s
            """
            cursor.execute(sql, (evento_id,))
            resultado = cursor.fetchone()

            if not resultado or all(v is None for v in resultado.values()):
                return None

            json_result = {
                "evento_id": evento_id,
                "media_nota_equipe": round(resultado['media_nota_equipe'], 2) if resultado['media_nota_equipe'] is not None else None,
                "media_nota_infraestrutura": round(resultado['media_nota_infraestrutura'], 2) if resultado['media_nota_infraestrutura'] is not None else None,
                "media_nota_organizacao": round(resultado['media_nota_organizacao'], 2) if resultado['media_nota_organizacao'] is not None else None,
                "media_nota_experiencia": round(resultado['media_nota_experiencia'], 2) if resultado['media_nota_experiencia'] is not None else None
            }
            return json_result
