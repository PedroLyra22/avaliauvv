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

    def media_por_estande(self, estande_id):
        with self.conn.cursor() as cursor:
            sql = """
                SELECT 
                    AVG(nota_apresentacao) AS media_apresentacao,
                    AVG(nota_ideia) AS media_nota_ideia,
                    AVG(nota_experiencia) AS media_nota_experiencia
                FROM avaliacao_estande
                WHERE estande_id = %s
            """
            cursor.execute(sql, (estande_id,))
            resultado = cursor.fetchone()

            if not resultado or all(v is None for v in resultado.values()):
                return None

            json_result = {
                "estande_id": estande_id,
                "media_apresentacao": round(resultado['media_apresentacao'], 2) if resultado['media_apresentacao'] is not None else None,
                "media_nota_ideia": round(resultado['media_nota_ideia'], 2) if resultado['media_nota_ideia'] is not None else None,
                "media_nota_experiencia": round(resultado['media_nota_experiencia'], 2) if resultado['media_nota_experiencia'] is not None else None
            }
            return json_result