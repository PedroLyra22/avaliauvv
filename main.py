from flask import Flask, jsonify, request

from avaliacao_estande_repository import AvaliacaoEstandeRepository
from avaliacao_evento_repository import AvaliacaoEventoRepository
from models import Endereco, Evento, Estande, AvaliacaoEvento, AvaliacaoEstande
from db import DB
from endereco_repository import EnderecoRepository
from evento_repository import EventoRepository
from estande_repository import EstandeRepository

app = Flask(__name__)

db = DB()

endereco_repo = EnderecoRepository(db)
evento_repo = EventoRepository(db)
estande_repo = EstandeRepository(db)
avaliacao_evento_repo = AvaliacaoEventoRepository(db)
avaliacao_estande_repo = AvaliacaoEstandeRepository(db)


# CRUD DE ENDEREÇO
@app.route('/endereco', methods=['POST'])
def criar_endereco():
    data = request.get_json()
    endereco = Endereco(
        id=None,
        cep=data['cep'],
        rua=data['rua'],
        bairro=data['bairro'],
        cidade=data['cidade'],
        numero=data['numero'],
        complemento=data.get('complemento')
    )
    endereco_repo.inserir(endereco)
    return jsonify({"message": "Endereço criado com sucesso!"}), 201

@app.route('/endereco', methods=['GET'])
def listar_enderecos():
    enderecos = endereco_repo.listar_todos()
    return jsonify(enderecos), 200

@app.route('/endereco/<int:id>', methods=['GET'])
def buscar_endereco(id):
    endereco = endereco_repo.buscar_por_id(id)
    if endereco:
        return jsonify({
            "id": endereco.id,
            "cep": endereco.cep,
            "rua": endereco.rua,
            "bairro": endereco.bairro,
            "cidade": endereco.cidade,
            "numero": endereco.numero,
            "complemento": endereco.complemento
        }), 200
    else:
        return jsonify({"message": "Endereço não encontrado"}), 404

@app.route('/endereco/<int:id>', methods=['DELETE'])
def deletar_endereco(id):
    endereco_repo.deletar(id)
    return jsonify({"message": "Endereço deletado com sucesso!"}), 200


# CRUD DE EVENTO
@app.route('/evento', methods=['POST'])
def criar_evento():
    data = request.get_json()
    evento = Evento(
        id=None,
        nome=data['nome'],
        data_inicial=data['data_inicial'],
        data_final=data['data_final'],
        imagem=data['imagem'],
        descricao=data['descricao'],
        endereco_id=data['endereco_id']
    )
    evento_repo.inserir(evento)
    return jsonify({"message": "Evento criado com sucesso!"}), 201

@app.route('/evento/<int:id>', methods=['DELETE'])
def deletar_evento(id):
    evento_repo.deletar(id)
    return jsonify({"message": "Evento deletado com sucesso!"}), 200


@app.route('/evento', methods=['GET'])
def listar_evaentos():
    eventos = evento_repo.listar_todos()
    if not eventos:
        return jsonify({"message": "Nenhum evento encontrado!"}), 404

    return jsonify([{
        "id": evento['id'],
        "nome": evento['nome'],
        "data_inicial": evento['data_inicial'],
        "data_final": evento['data_final'],
        "imagem": evento['imagem'],
        "descricao": evento['descricao'],
        "endereco_id": evento['endereco_id']
    } for evento in eventos]), 200


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
        evento_id=data['evento_id']
    )
    estande_repo.inserir(estande)
    return jsonify({"message": "Estande criado com sucesso!"}), 201

@app.route('/estande', methods=['GET'])
def listar_estandes():
    estandes = estande_repo.listar_todos()

    print(estandes)

    return jsonify([{
            "id": estande.get('id'),
            "nome": estande.get('nome'),
            "tema": estande.get('tema'),
            "imagem": estande.get('imagem'),
            "descricao": estande.get('descricao'),
            "evento_id": estande.get('evento_id')
        }
        for estande in estandes
    ]), 200

@app.route('/estande/<int:id>', methods=['DELETE'])
def deletar_estande(id):
    estande_repo.deletar(id)
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
    return jsonify({"message": "Avaliação do estande criada com sucesso!"}), 201


if __name__ == '__main__':
    app.run(debug=True)
