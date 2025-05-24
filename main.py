import os

from flask import Flask, jsonify, request, session
from flask_cors import CORS
from avaliacao_estande_repository import AvaliacaoEstandeRepository
from avaliacao_evento_repository import AvaliacaoEventoRepository
from models import Evento, Estande, AvaliacaoEvento, AvaliacaoEstande, AdminUser
from db import DB
from evento_repository import EventoRepository
from estande_repository import EstandeRepository
from admin_user_repository import AdminUserRepository

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

db = DB()

admin_repo = AdminUserRepository(db)
evento_repo = EventoRepository(db)
estande_repo = EstandeRepository(db)
avaliacao_evento_repo = AvaliacaoEventoRepository(db)
avaliacao_estande_repo = AvaliacaoEstandeRepository(db)

# CRUD ADMIN
@app.route('/admin/cadastrar', methods=['POST'])
def cadastrar_admin():
    data = request.json
    admin = AdminUser(
        id=None,
        login=data['login'],
        senha=data['senha'],
        email=data['email']
    )
    admin_repo.inserir(admin)
    return jsonify({"mensagem": "Admin cadastrado com sucesso"}), 201


@app.route('/admin/login', methods=['POST'])
def login_admin():
    data = request.json
    usuario = admin_repo.autenticar(data['login'], data['senha'])

    if usuario:
        session['admin_user_id'] = usuario['id']
        session['admin_user_login'] = usuario['login']
        return jsonify({"mensagem": "Login realizado com sucesso"}), 200
    return jsonify({"erro": "Login ou senha inválidos"}), 401


@app.route('/admin/deletar/<int:id>', methods=['DELETE'])
def deletar_admin(id):
    admin_repo.deletar(id)
    return jsonify({"mensagem": "Admin deletado com sucesso"}), 200


@app.route('/admin/sessao', methods=['GET'])
def info_sessao():
    if 'admin_user_id' in session:
        return jsonify({
            "id": session['admin_user_id'],
            "login": session['admin_user_login']
        })
    return jsonify({"erro": "NÃ£o autenticado"}), 401

# CRUD DE EVENTO
@app.route('/evento', methods=['POST'])
def criar_evento():
    data = request.get_json()

    if 'admin_user_id' not in data:
        return jsonify({"message": "admin_user_id não obrigatório"}), 400

    evento = Evento(
        id=None,
        nome=data['nome'],
        data_inicial=data['data_inicial'],
        data_final=data['data_final'],
        imagem=data['imagem'],
        descricao=data['descricao'],
        cep=data['cep'],
        rua=data['rua'],
        bairro=data['bairro'],
        cidade=data['cidade'],
        numero=data['numero'],
        complemento=data.get('complemento'),
        admin_user_id=data['admin_user_id']  # <- campo incluÃ­do
    )
    evento_repo.inserir(evento)
    return jsonify({"message": "Evento criado com sucesso!"}), 201


@app.route('/evento', methods=['GET'])
def listar_eventos():
    admin_user_id = request.args.get('admin_user_id', type=int)

    if not admin_user_id:
        return jsonify({"message": "admin_user_id não obrigatório"}), 400

    eventos = evento_repo.listar_todos(admin_user_id)

    if not eventos:
        return jsonify({"message": "Nenhum evento encontrado!"}), 404

    return jsonify([{
        "id": evento['id'],
        "nome": evento['nome'],
        "data_inicial": evento['data_inicial'],
        "data_final": evento['data_final'],
        "imagem": evento['imagem'],
        "descricao": evento['descricao'],
        "cep": evento['cep'],
        "rua": evento['rua'],
        "bairro": evento['bairro'],
        "cidade": evento['cidade'],
        "numero": evento['numero'],
        "complemento": evento['complemento']
    } for evento in eventos]), 200


@app.route('/evento/<int:id>', methods=['DELETE'])
def deletar_evento(id):
    data = request.get_json()
    admin_user_id = data.get('admin_user_id')

    if not admin_user_id:
        return jsonify({"message": "admin_user_id não obrigatório"}), 400

    evento_repo.deletar(id, admin_user_id)
    return jsonify({"message": "Evento deletado com sucesso!"}), 200

# CRUD DE ESTANDE
@app.route('/estande', methods=['POST'])
def criar_estande():
    data = request.get_json()
    estande = Estande(
        id=None,
        nome=data['nome'],
        tema=data['tema'],
        imagem=data['imagem'],
        descricao=data['descricao'],
        evento_id=data['evento_id'],
        admin_user_id=data['admin_user_id']  # <- campo adicionado
    )
    estande_repo.inserir(estande)
    return jsonify({"message": "Estande criado com sucesso!"}), 201


@app.route('/estande', methods=['GET'])
def listar_estandes():
    admin_user_id = request.args.get('admin_user_id', type=int)

    if not admin_user_id:
        return jsonify({"message": "admin_user_id não obrigatório"}), 400

    estandes = estande_repo.listar_todos(admin_user_id)

    return jsonify([{
        "id": estande.get('id'),
        "nome": estande.get('nome'),
        "tema": estande.get('tema'),
        "imagem": estande.get('imagem'),
        "descricao": estande.get('descricao'),
        "evento_id": estande.get('evento_id')
    } for estande in estandes]), 200


@app.route('/estande/<int:id>', methods=['DELETE'])
def deletar_estande(id):
    data = request.get_json()
    admin_user_id = data.get('admin_user_id')

    if not admin_user_id:
        return jsonify({"message": "admin_user_id não obrigatório"}), 400

    estande_repo.deletar(id, admin_user_id)
    return jsonify({"message": "Estande deletado com sucesso!"}), 200

#INSERT DE AVALIACAO DO EVENTO
@app.route('/avaliacao_evento', methods=['POST'])
def criar_avaliacao_evento():
    data = request.get_json()

    avaliacao = AvaliacaoEvento(
        id=None,
        nota_equipe=data['nota_equipe'],
        nota_infraestrutura=data['nota_infraestrutura'],
        nota_organizacao=data['nota_organizacao'],
        nota_experiencia=data['nota_experiencia'],
        imagem_avaliacao=data.get('imagem_avaliacao'),
        evento_id=data['evento_id']
    )

    avaliacao_evento_repo.inserir(avaliacao)
    return jsonify({"message": "Avaliação criada com sucesso!"}), 201

@app.route('/avaliacao_estande', methods=['POST'])
def criar_avaliacao_estande():
    data = request.get_json()

    avaliacao_estande = AvaliacaoEstande(
        id=None,
        nota_apresentacao=data['nota_apresentacao'],
        nota_ideia=data['nota_ideia'],
        nota_experiencia=data['nota_experiencia'],
        imagem_avaliacao=data.get('imagem_avaliacao'),
        estande_id=data['estande_id']
    )

    avaliacao_estande_repo.inserir(avaliacao_estande)
    return jsonify({"message": "AvaliaÃ§Ã£o do estande criada com sucesso!"}), 201



if __name__ == '__main__':
    app.run(debug=True)