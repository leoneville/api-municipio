from factory import db

class Estado(db.Model):
    __tablename__ = "estado"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sigla = db.Column(db.String(2), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'sigla': self.sigla}
    
    def __repr__(self) -> str:
        return f"<Estado {self.nome}>"