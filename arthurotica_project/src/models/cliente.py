from src.models.user import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date, nullable=True)
    endereco = db.Column(db.String(300), nullable=True)
    bairro = db.Column(db.String(100), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    
    def to_dict(self):
        return {
            'ID_NOME_CLIENTE': f'{self.id} - {self.nome}',
            'CPF': self.cpf,
            'DATA NASCIMENTO': self.data_nascimento.strftime('%Y-%m-%d') if self.data_nascimento else None,
            'ENDEREÇO': self.endereco,
            'BAIRRO': self.bairro,
            'CIDADE': self.cidade,
            'TELEFONE': self.telefone
        }

