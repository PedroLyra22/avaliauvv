from models import AdminUser

class AdminUserRepository:
    def __init__(self, db):
        self.conn = db.get_conn()

    def inserir(self, admin_user):
        senha_hash = AdminUser.gerar_hash_senha(admin_user.senha)
        with self.conn.cursor() as cursor:
            sql = """
                INSERT INTO admin_user (login, senha, email)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (
                admin_user.login,
                senha_hash,
                admin_user.email
            ))
        self.conn.commit()

    def deletar(self, admin_user_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM admin_user WHERE id = %s"
            cursor.execute(sql, (admin_user_id,))
        self.conn.commit()

    def autenticar(self, login, senha):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM admin_user WHERE login = %s"
            cursor.execute(sql, (login,))
            usuario = cursor.fetchone()

            if usuario and AdminUser.verificar_senha(senha, usuario['senha']):
                return usuario
            return None