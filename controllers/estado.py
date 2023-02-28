from flask import Blueprint, jsonify
from factory import api, db
from models import Estado, Municipio
from spectree import Response

estado_controller = Blueprint('estado_controller', __name__, url_prefix='/api')

@estado_controller.get('/estados')
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None, HTTP_404=None), tags=["Estados"])
def listar_estados():
    '''
    Listagem de estados
    '''
    estados = Estado.query.all()

    return jsonify([estado.to_dict() for estado in estados]), 200

@estado_controller.get('/estados/<int:estado_id>/municipios')
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None, HTTP_404=None), tags=["Estados"])
def listar_municipios_por_estado(estado_id):
    '''
    Listagem de municípios de um estado
    '''
    municipios = Municipio.query.filter_by(id_estado=estado_id).all()
    if not municipios:
        return jsonify({'erro': 'Estado não encontrado.'}), 404

    return jsonify([{'id': municipio.id, 'nome': municipio.nome} for municipio in municipios])