import bcrypt

class AdminUser:
    def __init__(self, id, login, senha, email):
        self.id = id
        self.login = login
        self.senha = senha
        self.email = email

    @staticmethod
    def gerar_hash_senha(senha_plana):
        return bcrypt.hashpw(senha_plana.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def verificar_senha(senha_plana, senha_hash):
        return bcrypt.checkpw(senha_plana.encode(), senha_hash.encode())

class Evento:
    def __init__(self, id, nome, data_inicial, data_final, imagem, descricao, cep, rua, bairro, cidade, numero,
                 complemento=None, admin_user_id=None):
        self.id = id
        self.nome = nome
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.imagem = imagem
        self.descricao = descricao
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero = numero
        self.complemento = complemento
        self.admin_user_id = admin_user_id


class Estande:
    def __init__(self, id, nome, tema, imagem, descricao, evento_id, admin_user_id=None):
        self.id = id
        self.nome = nome
        self.tema = tema
        self.imagem = imagem
        self.descricao = descricao
        self.evento_id = evento_id
        self.admin_user_id = admin_user_id


class AvaliacaoEvento:
    def __init__(self, id, nota_equipe, nota_infraestrutura, nota_organizacao, nota_experiencia, evento_id):
        self.id = id
        self.nota_equipe = nota_equipe
        self.nota_infraestrutura = nota_infraestrutura
        self.nota_organizacao = nota_organizacao
        self.nota_experiencia = nota_experiencia
        self.evento_id = evento_id


class AvaliacaoEstande:
    def __init__(self, id, nota_apresentacao, nota_ideia, nota_experiencia, estande_id):
        self.id = id
        self.nota_apresentacao = nota_apresentacao
        self.nota_ideia = nota_ideia
        self.nota_experiencia = nota_experiencia
        self.estande_id = estande_id