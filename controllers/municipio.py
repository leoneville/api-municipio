from flask import Blueprint, jsonify, request
from factory import api, db
from models import Estado, Municipio
from models.municipio import CriarMunicipio, AtualizarMunicipio
from spectree import Response

municipio_controller = Blueprint('municipio_controller', __name__, url_prefix='/api')

@municipio_controller.post('/municipios')
@api.validate(json=CriarMunicipio, resp=Response(HTTP_201=None), tags=["Municípios"])
def criar_municipio():
    '''
    Criação de um município
    '''
    if not request.json or not 'nome' in request.json or not 'id_estado' in request.json:
        return jsonify({'erro': 'Dados inválidos.'}), 400

    nome = request.json['nome']
    id_estado = request.json['id_estado']

    estado = Estado.query.get(id_estado)

    if not estado:
        return jsonify({'erro': 'Estado não encontrado.'}), 404

    municipio = Municipio(nome=nome, id_estado=id_estado)

    try:
        db.session.add(municipio)
        db.session.commit()
    except:
        db.session.rollback()
        return {"msg": "Ops! Something went wrong."}, 400

    return jsonify(municipio.to_dict()), 201


@municipio_controller.put('/municipios/<int:municipio_id>')
@api.validate(json=AtualizarMunicipio, resp=Response(HTTP_200=None, HTTP_404=None), tags=["Municípios"])
def atualizar_municipio(municipio_id):
    '''
    Atualização de um município
    '''
    municipio = Municipio.query.filter_by(id=municipio_id).first()

    if not municipio:
        return jsonify({'erro': 'Município não encontrado.'}), 404

    nome = request.json.get('nome')

    if not nome:
        return jsonify({'erro': 'Nome do município não fornecido.'}), 400

    municipio.nome = nome

    try:
        db.session.add(municipio)
        db.session.commit()
    except:
        db.session.rollback()
        return {"msg": "Ops! Something went wrong."}, 400

    return jsonify({'mensagem': 'Município atualizado com sucesso.'}), 200


@municipio_controller.delete('/municipios/<int:municipio_id>')
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None, HTTP_404=None), tags=["Municípios"])
def excluir_municipio(municipio_id):
    '''
    Exclusão de um município
    '''
    municipio = Municipio.query.filter_by(id=municipio_id).first()

    if not municipio:
        return jsonify({'erro': 'Município não encontrado.'}), 404
    
    try:
        db.session.delete(municipio)
        db.session.commit()
    except:
        db.session.rollback()
        return {"msg": "Ops! Something went wrong."}, 400

    return jsonify({'mensagem': 'Município excluído com sucesso.'}), 200