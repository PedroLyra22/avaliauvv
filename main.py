from flask import Flask, jsonify, request

from models import Endereco, Evento
from db import DB
from endereco_repository import EnderecoRepository
from evento_repository import EventoRepository

app = Flask(__name__)

db = DB()

endereco_repo = EnderecoRepository(db)
evento_repo = EventoRepository(db)

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
def listar_eventos():
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


if __name__ == '__main__':
    app.run(debug=True)
