from models import Endereco


class EnderecoRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, endereco):
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO endereco (cep, rua, bairro, cidade, numero, complemento)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                endereco.cep,
                endereco.rua,
                endereco.bairro,
                endereco.cidade,
                endereco.numero,
                endereco.complemento
            ))
        self.conn.commit()

    def listar_todos(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM endereco")
            return cursor.fetchall()

    def atualizar(self, endereco):
        with self.conn.cursor() as cursor:
            sql = """
                UPDATE endereco SET cep = %s, rua = %s, bairro = %s, cidade = %s, numero = %s, complemento = %s
                WHERE id = %s
            """
            cursor.execute(sql, (
                endereco.cep,
                endereco.rua,
                endereco.bairro,
                endereco.cidade,
                endereco.numero,
                endereco.complemento,
                endereco.id
            ))
        self.conn.commit()

    def buscar_por_id(self, id):
        with self.conn.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM endereco WHERE id = %s"
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()

            if resultado:
                endereco = Endereco(
                    id=resultado['id'],
                    cep=resultado['cep'],
                    rua=resultado['rua'],
                    bairro=resultado['bairro'],
                    cidade=resultado['cidade'],
                    numero=resultado['numero'],
                    complemento=resultado['complemento']
                )
                return endereco
            else:
                return None

    def deletar(self, endereco_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM endereco WHERE id = %s"
            cursor.execute(sql, (endereco_id,))
        self.conn.commit()