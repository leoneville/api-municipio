from factory import db
from pydantic import BaseModel

class Municipio(db.Model):
    __tablename__ = 'municipio'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id'), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'id_estado': self.id_estado}
    
    def __repr__(self) -> str:
        return f"<Municipio {self.nome}>"
    
class CriarMunicipio(BaseModel):
    nome: str
    id_estado: int

class AtualizarMunicipio(BaseModel):
    nome: str
    
