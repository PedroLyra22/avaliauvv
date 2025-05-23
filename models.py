class Evento:
    def __init__(self, id, nome, data_inicial, data_final, imagem, descricao, cep, rua, bairro, cidade, numero, complemento=None, admin_user_id=None):
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
        self.admin_user_id = admin_user_id
        self.evento_id = evento_id


class AvaliacaoEvento:
    def __init__(self, id, nota_equipe, nota_infraestrutura, nota_organizacao, nota_experiencia, imagem_avaliacao, evento_id):
        self.id = id
        self.nota_equipe = nota_equipe
        self.nota_infraestrutura = nota_infraestrutura
        self.nota_organizacao = nota_organizacao
        self.nota_experiencia = nota_experiencia
        self.imagem_avaliacao = imagem_avaliacao
        self.evento_id = evento_id


class AvaliacaoEstande:
    def __init__(self, id, nota_apresentacao, nota_ideia, nota_experiencia, imagem_avaliacao, estande_id):
        self.id = id
        self.nota_apresentacao = nota_apresentacao
        self.nota_ideia = nota_ideia
        self.nota_experiencia = nota_experiencia
        self.imagem_avaliacao = imagem_avaliacao
        self.estande_id = estande_id