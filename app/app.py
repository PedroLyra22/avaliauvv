from flask import Flask, jsonify, request

from repositories.endereco_repository import EnderecoRepository
from models import Endereco
from db import DB


app = Flask(__name__)

db = DB()

endereco_repo = EnderecoRepository(db)

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

@app.route('/endereco/<int:id>', methods=['PUT'])
def atualizar_endereco(id):
    data = request.get_json()
    endereco = Endereco(
        id=id,
        cep=data['cep'],
        rua=data['rua'],
        bairro=data['bairro'],
        cidade=data['cidade'],
        numero=data['numero'],
        complemento=data.get('complemento')
    )
    endereco_repo.atualizar(endereco)
    return jsonify({"message": "Endereço atualizado com sucesso!"}), 200

@app.route('/endereco/<int:id>', methods=['DELETE'])
def deletar_endereco(id):
    endereco_repo.deletar(id)
    return jsonify({"message": "Endereço deletado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
